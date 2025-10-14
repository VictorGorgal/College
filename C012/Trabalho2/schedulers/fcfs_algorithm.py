from .base_algorithm import BaseAlgorithm


class FCFSAlgorithm(BaseAlgorithm):
    def get_next_job(self, job_queue):
        return job_queue.pop(0)
