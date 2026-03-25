import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        
        min_heap = []
        current_max = float('-inf')
        
        for i in range(k):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
            
        min_range_start = -1000000001
        min_range_end = 1000000001
        
        while len(min_heap) == k:
            min_val, list_idx, element_idx = heapq.heappop(min_heap)
            
            if (current_max - min_val < min_range_end - min_range_start) or \
               (current_max - min_val == min_range_end - min_range_start and min_val < min_range_start):
                min_range_start = min_val
                min_range_end = current_max
            
            if element_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][element_idx + 1]
                heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
                current_max = max(current_max, next_val)
            else:
                break
                
        return [min_range_start, min_range_end]
