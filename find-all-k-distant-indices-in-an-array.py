from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        left = [10**9] * n
        last = -1
        for i in range(n):
            if nums[i] == key:
                last = i
                left[i] = 0
            elif last != -1:
                left[i] = i - last
        right = [10**9] * n
        nxt = -1
        for i in range(n - 1, -1, -1):
            if nums[i] == key:
                nxt = i
                right[i] = 0
            elif nxt != -1:
                right[i] = nxt - i
        res = []
        for i in range(n):
            if min(left[i], right[i]) <= k:
                res.append(i)
        return res
