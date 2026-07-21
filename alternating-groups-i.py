from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        for i in range(n):
            mid = colors[(i+1) % n]
            if mid != colors[i] and mid != colors[(i+2) % n]:
                count += 1
        return count
