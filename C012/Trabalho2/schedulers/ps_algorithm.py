from .base_algorithm import BaseAlgorithm


class PSAlgorithm(BaseAlgorithm):
    def get_next_job(self, job_queue: list):
        shortest_job = max(job_queue, key=lambda job: job.priority)
        job_queue.remove(shortest_job)
        return shortest_job
