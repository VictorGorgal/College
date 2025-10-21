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
            job = self.manager.get_next_job()
            if not job:
                break

            # Calcula o tempo que o processo demorou para ser executado
            wait_time = time.time() - self.manager.start_time

            # Simula tempo para inicializar processo
            time.sleep(random.uniform(0, 0.2))

            # Simula processamento que nao depende do recurso critico
            self.manager.worker_status[self.wid] = "Processing data..."
            time.sleep(1.5)

            self.current_job = job
            if self.semaphore:
                wait_start = time.time()
                self.manager.worker_status[self.wid] = "Waiting semaphore..."
                with self.semaphore:
                    wait_end = time.time()
                    semaphore_wait_time = wait_end - wait_start
                    self._execute(job, wait_time + semaphore_wait_time)
            else:
                self._execute(job, wait_time)

            self.current_job = None

    def _execute(self, job, wait_time):
        self.manager.worker_status[self.wid] = f"printing \"{job}\""
        job.execute(self.manager.buffer)
        self.manager.worker_status[self.wid] = "idle"
        self.manager.worker_history[self.wid].append(f'Espera: {wait_time:.3f}s, Prioridade: {job.priority}, Texto: \"{job}\"')
        self.manager.total_wait_time += wait_time
