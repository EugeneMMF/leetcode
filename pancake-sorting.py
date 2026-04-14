from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_val = size
            idx = arr.index(max_val)
            if idx == size - 1:
                continue
            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])
            res.append(size)
            arr[:size] = reversed(arr[:size])
        return res
