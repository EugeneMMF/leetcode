from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_d = releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            d = releaseTimes[i] - releaseTimes[i-1]
            if d > max_d or (d == max_d and keysPressed[i] > ans):
                max_d = d
                ans = keysPressed[i]
        return ans
