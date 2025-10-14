import threading

from utils.display_thread import DisplayThread


class ProcessManager:
    def __init__(self, algorithm, processes, workers, use_semaphore=False):
        self.algorithm = algorithm
        self.processes = processes
        self.buffer = []
        self.worker_status = {i: "idle" for i in range(len(workers))}
        self.worker_history = {i: [] for i in range(len(workers))}
        self.job_queue = list(processes)
        self.use_semaphore = use_semaphore
        self.semaphore = threading.Semaphore(1) if use_semaphore else None
        self.workers = workers

    def get_next_job(self):
        if not self.job_queue:
            return None
        return self.algorithm.get_next_job(self.job_queue)

    def run(self):
        display = DisplayThread(self.buffer, len(self.processes), self.worker_status, self.worker_history)
        display.start()

        self._configureWorkers()

        threads = []
        for worker in self.workers:
            worker.start()
            threads.append(worker)
        for t in threads:
            t.join()

        display.stop()

    def _configureWorkers(self):
        for worker in self.workers:
            worker.manager = self
            worker.semaphore = self.semaphore
