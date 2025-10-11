import threading
import time
import random
from queue import Queue
from threading import Lock

print_log = []
log_lock = Lock()


class PrintJob:
    def __init__(self, job_id, pages, priority=1):
        self.job_id = job_id
        self.pages = pages
        self.priority = priority

    def __repr__(self):
        return f"Job-{self.job_id} ({self.pages} pages, P{self.priority})"


def printer_without_control(printer_id, jobs):
    for job in jobs:
        time.sleep(random.uniform(0.05, 0.15))
        entry = f"Printer {printer_id} finished {job}\n"
        for ch in entry:
            print_log.append(ch)
            time.sleep(0.001)


def printer_with_control(printer_id, job_queue: Queue):
    while True:
        try:
            job = job_queue.get_nowait()
        except:
            break
        time.sleep(job.pages * 0.05)
        with log_lock:
            entry = f"Printer {printer_id} finished {job}\n"
            for ch in entry:
                print_log.append(ch)
                time.sleep(0.001)
        job_queue.task_done()


def run_without_scheduling():
    global print_log
    print_log = []

    jobs = [PrintJob(i, random.randint(1, 4)) for i in range(4)]
    printers = [threading.Thread(target=printer_without_control, args=(i, jobs)) for i in range(2)]

    for p in printers:
        p.start()
    for p in printers:
        p.join()

    print("\n--- LOG WITHOUT SYNCHRONIZATION ---")
    print("".join(print_log))


def run_with_scheduling():
    global print_log
    print_log = []

    jobs = [PrintJob(i, random.randint(1, 4)) for i in range(4)]
    job_queue = Queue()
    for job in jobs:
        job_queue.put(job)

    printers = [threading.Thread(target=printer_with_control, args=(i, job_queue)) for i in range(2)]

    for p in printers:
        p.start()
    for p in printers:
        p.join()

    print("\n--- LOG WITH SYNCHRONIZATION ---")
    print("".join(print_log))


if __name__ == "__main__":
    run_without_scheduling()
    run_with_scheduling()
