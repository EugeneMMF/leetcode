from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        prev = {}
        for num in nums:
            curr = {num: 1}
            for val, cnt in prev.items():
                new_val = val & num
                curr[new_val] = curr.get(new_val, 0) + cnt
            res += curr.get(k, 0)
            prev = curr
        return res
