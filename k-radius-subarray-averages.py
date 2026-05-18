from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return nums[:]
        window = 2 * k + 1
        if window > n:
            return [-1] * n
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        res = [-1] * n
        for i in range(k, n - k):
            total = pref[i + k + 1] - pref[i - k]
            res[i] = total // window
        return res