class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = []
        for i in range(len(difficulty)):
            jobs.append((difficulty[i], profit[i]))
        
        jobs.sort()

        worker.sort()

        total_profit = 0
        current_max_profit_for_available_jobs = 0
        job_pointer = 0
        num_jobs = len(jobs)

        for w_ability in worker:
            while job_pointer < num_jobs and jobs[job_pointer][0] <= w_ability:
                current_max_profit_for_available_jobs = max(
                    current_max_profit_for_available_jobs,
                    jobs[job_pointer][1]
                )
                job_pointer += 1
            
            total_profit += current_max_profit_for_available_jobs
        
        return total_profit
