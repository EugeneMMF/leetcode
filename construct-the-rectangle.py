import math

class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        w_max = int(math.sqrt(area))
        
        for w in range(w_max, 0, -1):
            if area % w == 0:
                l = area // w
                return [l, w]
