import bisect
from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        la = len(a)
        lb = len(b)
        a_indices = []
        b_indices = []
        for i in range(n - la + 1):
            if s[i:i+la] == a:
                a_indices.append(i)
        for j in range(n - lb + 1):
            if s[j:j+lb] == b:
                b_indices.append(j)
        res = []
        for i in a_indices:
            left = bisect.bisect_left(b_indices, i - k)
            if left < len(b_indices) and abs(b_indices[left] - i) <= k:
                res.append(i)
            elif left + 1 < len(b_indices) and abs(b_indices[left + 1] - i) <= k:
                res.append(i)
        return res
