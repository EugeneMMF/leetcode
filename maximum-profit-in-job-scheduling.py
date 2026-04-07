import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        n = len(startTime)
        
        jobs = []
        for i in range(n):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort()

        sorted_start_times = [job[0] for job in jobs]

        memo = {}

        def find_next_valid_job_index(current_end_time, search_start_index):
            idx = bisect.bisect_left(sorted_start_times, current_end_time, lo=search_start_index)
            return idx

        def get_max_profit(index):
            if index == n:
                return 0
            if index in memo:
                return memo[index]

            profit_without_current = get_max_profit(index + 1)

            current_job_end, current_job_profit = jobs[index][1], jobs[index][2]
            
            next_job_idx = find_next_valid_job_index(current_job_end, index + 1)
            
            profit_with_current = current_job_profit + get_max_profit(next_job_idx)

            memo[index] = max(profit_without_current, profit_with_current)
            return memo[index]

        return get_max_profit(0)
