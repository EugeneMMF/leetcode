from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d < min_diff:
                min_diff = d
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                res.append([arr[i-1], arr[i]])
        return res
