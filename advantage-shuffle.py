import sys
from typing import List
from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        dq = deque(sorted(nums1))
        idxs = sorted(range(n), key=lambda i: -nums2[i])
        res = [0] * n
        for i in idxs:
            if dq[-1] > nums2[i]:
                res[i] = dq.pop()
            else:
                res[i] = dq.popleft()
        return res
