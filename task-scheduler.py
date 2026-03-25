import collections

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = collections.Counter(tasks)

        max_freq = 0
        for count in task_counts.values():
            max_freq = max(max_freq, count)
        
        count_max_freq = 0
        for count in task_counts.values():
            if count == max_freq:
                count_max_freq += 1
        
        time_based_on_cooling = (max_freq - 1) * (n + 1) + count_max_freq

        return max(time_based_on_cooling, len(tasks))
