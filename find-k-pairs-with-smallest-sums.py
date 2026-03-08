import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        result = []
        min_heap = []
        
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            
        while min_heap and len(result) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j + 1))
                
        return result
