import bisect
from typing import List

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        def sums(arr):
            res = [0]
            for x in arr:
                res += [s + x for s in res]
            return res
        sums_left = sums(left)
        sums_right = sums(right)
        sums_right.sort()
        best = abs(goal)
        for sl in sums_left:
            target = goal - sl
            i = bisect.bisect_left(sums_right, target)
            if i < len(sums_right):
                best = min(best, abs(sl + sums_right[i] - goal))
            if i > 0:
                best = min(best, abs(sl + sums_right[i-1] - goal))
        return best