from typing import List

class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        cost_no = sum(abs(a - b) for a, b in zip(arr, brr))
        sorted_arr = sorted(arr)
        sorted_brr = sorted(brr)
        cost_reorder = sum(abs(a - b) for a, b in zip(sorted_arr, sorted_brr)) + k
        return min(cost_no, cost_reorder)
