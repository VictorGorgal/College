import threading
import time


class DisplayThread(threading.Thread):
    def __init__(self, buffer, maxBufferSize, worker_status, worker_history, refresh_rate=0.1):
        super().__init__(daemon=True)
        self.buffer = buffer
        self.maxBufferSize = maxBufferSize
        self.worker_status = worker_status
        self.worker_history = worker_history
        self.refresh_rate = refresh_rate
        self.running = True

    def _print(self):
        output = "".join(self.buffer)
        print("\033c", end="")

        print("--- BUFFER ---")
        print(output.strip())
        print('\n' * (self.maxBufferSize - len(output.strip().split('\n'))))

        print("\n--- PRINTER STATUS ---")
        for pid, status in self.worker_status.items():
            print(f"Printer {pid}: {status}")

        print("\n--- PROCESS HISTORY ---")
        for pid, status in self.worker_history.items():
            print(f'\n# Printer {pid}:')
            for id, stat in enumerate(status):
                print(stat)

    def run(self):
        while self.running:
            self._print()
            time.sleep(self.refresh_rate)

    def stop(self):
        self.running = False
        self._print()
