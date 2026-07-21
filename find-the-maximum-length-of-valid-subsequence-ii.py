from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = [{} for _ in range(n)]
        ans = 1
        for i in range(n):
            for j in range(i):
                c = (nums[j] + nums[i]) % k
                prev = best[j].get(c, 1)
                cur = prev + 1
                if cur > best[i].get(c, 0):
                    best[i][c] = cur
                    if cur > ans:
                        ans = cur
        return ans
