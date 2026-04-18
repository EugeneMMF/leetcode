from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        seq = [i ^ (i >> 1) for i in range(1 << n)]
        idx = seq.index(start)
        return seq[idx:] + seq[:idx]
