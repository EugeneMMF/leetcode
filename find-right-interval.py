import bisect

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        start_indices = []
        for i in range(n):
            start_indices.append((intervals[i][0], i))
        
        start_indices.sort()
        
        sorted_starts_only = [item[0] for item in start_indices]
        
        result = [-1] * n
        
        for i in range(n):
            current_end = intervals[i][1]
            
            idx = bisect.bisect_left(sorted_starts_only, current_end)
            
            if idx < n:
                result[i] = start_indices[idx][1]
                
        return result
