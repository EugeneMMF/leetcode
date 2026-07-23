from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * (n - k + 1)
        for i in range(n - k + 1):
            ok = True
            for j in range(i, i + k - 1):
                if nums[j + 1] - nums[j] != 1:
                    ok = False
                    break
            if ok:
                res[i] = nums[i + k - 1]
        return res
