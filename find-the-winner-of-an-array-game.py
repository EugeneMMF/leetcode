from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        champion = arr[0]
        win = 0
        for x in arr[1:]:
            if champion > x:
                win += 1
            else:
                champion = x
                win = 1
            if win == k:
                return champion
        return champion
