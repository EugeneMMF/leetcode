from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        diff = [1 if colors[i] != colors[(i + 1) % n] else 0 for i in range(n)]
        diff2 = diff + diff
        window = k - 1
        cur = sum(diff2[:window])
        count = 0
        for i in range(n):
            if cur == window:
                count += 1
            cur += diff2[i + window] - diff2[i]
        return count
