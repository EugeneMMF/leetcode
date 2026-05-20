import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left = [0] * (3 * n)
        right = [0] * (3 * n)

        max_heap = []
        s = 0
        for i in range(n):
            heapq.heappush(max_heap, -nums[i])
            s += nums[i]
        left[n - 1] = s
        for i in range(n, 2 * n):
            if nums[i] < -max_heap[0]:
                s += nums[i] + heapq.heapreplace(max_heap, -nums[i])
            left[i] = s

        min_heap = []
        s = 0
        for i in range(3 * n - 1, 3 * n - n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            s += nums[i]
        right[2 * n] = s
        for i in range(2 * n - 1, n - 1, -1):
            if nums[i] > min_heap[0]:
                s += nums[i] - heapq.heapreplace(min_heap, nums[i])
            right[i] = s

        ans = float('inf')
        for i in range(n - 1, 2 * n):
            ans = min(ans, left[i] - right[i + 1])
        return ans
