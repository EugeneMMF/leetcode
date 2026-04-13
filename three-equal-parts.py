from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        total = sum(arr)
        if total == 0:
            return [0, n - 1]
        if total % 3 != 0:
            return [-1, -1]
        k = total // 3
        first = second = third = -1
        cnt = 0
        for i, v in enumerate(arr):
            if v == 1:
                cnt += 1
                if cnt == 1:
                    first = i
                elif cnt == k + 1:
                    second = i
                elif cnt == 2 * k + 1:
                    third = i
        while third < n and arr[first] == arr[second] == arr[third]:
            first += 1
            second += 1
            third += 1
        if third == n:
            return [first - 1, second]
        return [-1, -1]
