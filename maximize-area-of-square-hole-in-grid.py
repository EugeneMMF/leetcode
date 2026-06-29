class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        max_h = 0
        cur = 0
        prev = None
        for bar in hBars:
            if prev is None or bar != prev + 1:
                cur = 1
            else:
                cur += 1
            if cur > max_h:
                max_h = cur
            prev = bar
        maxRows = max_h + 1
        vBars.sort()
        max_v = 0
        cur = 0
        prev = None
        for bar in vBars:
            if prev is None or bar != prev + 1:
                cur = 1
            else:
                cur += 1
            if cur > max_v:
                max_v = cur
            prev = bar
        maxCols = max_v + 1
        side = min(maxRows, maxCols)
        return side * side