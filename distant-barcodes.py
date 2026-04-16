from collections import Counter
from typing import List

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        items = sorted(cnt.items(), key=lambda x: -x[1])
        res = [0] * len(barcodes)
        idx = 0
        for val, freq in items:
            for _ in range(freq):
                res[idx] = val
                idx += 2
                if idx >= len(barcodes):
                    idx = 1
        return res
