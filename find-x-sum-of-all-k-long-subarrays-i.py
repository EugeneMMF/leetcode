from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = {}
            for v in window:
                freq[v] = freq.get(v, 0) + 1
            if len(freq) <= x:
                res.append(sum(window))
                continue
            items = sorted(freq.items(), key=lambda kv: (-kv[1], -kv[0]))
            keep = items[:x]
            s = sum(v * c for v, c in keep)
            res.append(s)
        return res