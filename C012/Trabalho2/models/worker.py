import random
import threading
import time


class Worker(threading.Thread):
    def __init__(self, wid, process_manager=None, semaphore=None):
        super().__init__(daemon=True)
        self.wid = wid
        self.manager = process_manager
        self.semaphore = semaphore
        self.current_job = None

    def run(self):
        while True:
            # Simula tempo para inicializar processo
            time.sleep(random.uniform(0, 0.2))

            job = self.manager.get_next_job()
            if not job:
                break

            # Simula processamento que nao depende do recurso critico
            self.manager.worker_status[self.wid] = "Processing data..."
            time.sleep(1.5)

            self.current_job = job
            if self.semaphore:
                wait_start = time.time()
                self.manager.worker_status[self.wid] = "Waiting semaphore..."
                with self.semaphore:
                    wait_end = time.time()
                    self._execute(job, wait_end - wait_start)
            else:
                self._execute(job, 0)

            self.current_job = None

    def _execute(self, job, wait_time):
        self.manager.worker_status[self.wid] = f"printing \"{job}\""
        job.execute(self.manager.buffer)
        self.manager.worker_status[self.wid] = "idle"
        self.manager.worker_history[self.wid].append(f'Espera: {wait_time:.3f}s, Prioridade: {job.priority}, Texto: \"{job}\"')
        self.manager.total_wait_time += wait_time
