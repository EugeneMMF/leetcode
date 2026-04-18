from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = {0: 1}
        odd = 0
        res = 0
        for v in nums:
            odd += v & 1
            res += cnt.get(odd - k, 0)
            cnt[odd] = cnt.get(odd, 0) + 1
        return res
