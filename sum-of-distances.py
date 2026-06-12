from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        res = [0] * len(nums)
        for idxs in groups.values():
            k = len(idxs)
            if k <= 1:
                continue
            prefix = [0] * k
            prefix[0] = idxs[0]
            for i in range(1, k):
                prefix[i] = prefix[i - 1] + idxs[i]
            total = prefix[-1]
            for i, pos in enumerate(idxs):
                left = pos * i - (prefix[i - 1] if i > 0 else 0)
                right = (total - prefix[i]) - pos * (k - 1 - i)
                res[pos] = left + right
        return res
