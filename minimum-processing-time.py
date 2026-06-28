class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        max_time = 0
        for i in range(len(processorTime)):
            max_task = tasks[i * 4]
            max_time = max(max_time, processorTime[i] + max_task)
        return max_time