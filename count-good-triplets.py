from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n - 2):
            ai = arr[i]
            for j in range(i + 1, n - 1):
                aj = arr[j]
                if abs(ai - aj) > a:
                    continue
                for k in range(j + 1, n):
                    ak = arr[k]
                    if abs(aj - ak) <= b and abs(ai - ak) <= c:
                        cnt += 1
        return cnt
