from .base_algorithm import BaseAlgorithm


class SJFAlgorithm(BaseAlgorithm):
    def get_next_job(self, job_queue: list):
        shortest_job = min(job_queue, key=lambda job: job.length)
        job_queue.remove(shortest_job)
        return shortest_job
