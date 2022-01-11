class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

    def get_job_id(self):
        return self.job_id

    def get_deadline(self):
        return self.deadline

    def get_profit(self):
        return self.profit


def get_max_profit_from_jobs(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_jobs = [-1 for _ in jobs]

    max_profit = 0
    for job in jobs:
        for i in range(job.deadline - 1, -1, -1):
            if max_jobs[i] == -1:
                max_jobs[i] = job.job_id
                max_profit += job.profit
                break

    print(max_jobs)
    print(max_profit)


if __name__ == '__main__':
    j1 = Job(1, 3, 35)
    j2 = Job(2, 4, 30)
    j5 = Job(5, 3, 15)
    j6 = Job(6, 1, 12)
    j7 = Job(7, 2, 5)

    jobs = [j1, j2, j5, j6, j7]
    get_max_profit_from_jobs(jobs)


