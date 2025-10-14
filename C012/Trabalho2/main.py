from models.print_job import phrases
from models.process import Process
from models.worker import Worker
from process_manager import ProcessManager
import schedulers
import random


if __name__ == "__main__":
    random.shuffle(phrases)
    processes = [
        Process(i, phrases[i], priority=i % 3 + 1, charsPerSecond=20)
        for i in range(6)
    ]

    manager = ProcessManager(
        algorithm=schedulers.FCFSAlgorithm(),
        processes=processes,
        workers=[
            Worker(0),
            Worker(1),
        ],
        use_semaphore=True
    )

    manager.run()
