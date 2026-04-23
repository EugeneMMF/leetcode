from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sorted_arr = sorted(arr)
        m = (len(arr) - 1) // 2
        centre = sorted_arr[m]
        strongest = sorted(arr, key=lambda x: (abs(x - centre), x), reverse=True)
        return strongest[:k]
