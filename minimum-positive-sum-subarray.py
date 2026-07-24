from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        INF = 10**18
        ans = INF
        for i in range(1, n+1):
            for length in range(l, r+1):
                j = i - length
                if j < 0:
                    break
                s = prefix[i] - prefix[j]
                if s > 0 and s < ans:
                    ans = s
        return -1 if ans == INF else ans
