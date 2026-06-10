from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        count = [0] * n
        end = 0
        for i in range(n):
            while end < n and prizePositions[end] <= prizePositions[i] + k:
                end += 1
            count[i] = end - i
        best_suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best_suffix[i] = max(count[i], best_suffix[i + 1])
        max_win = 0
        end = 0
        for i in range(n):
            while end < n and prizePositions[end] <= prizePositions[i] + k:
                end += 1
            max_win = max(max_win, count[i] + best_suffix[end])
        return max_win