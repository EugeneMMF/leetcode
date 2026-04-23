class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        MOD = 10**9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            gap = horizontalCuts[i] - horizontalCuts[i - 1]
            if gap > max_h:
                max_h = gap
        max_v = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            gap = verticalCuts[i] - verticalCuts[i - 1]
            if gap > max_v:
                max_v = gap
        return (max_h * max_v) % MOD
