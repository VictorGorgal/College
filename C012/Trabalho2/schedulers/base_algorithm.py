from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):
    @abstractmethod
    def get_next_job(self, job_queue):
        """Return the next job based on the algorithm’s logic."""
        pass
