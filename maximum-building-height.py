class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)
        pos = [0] * m
        h = [0] * m
        for i, (p, hi) in enumerate(restrictions):
            pos[i] = p
            h[i] = hi
        for i in range(1, m):
            d = pos[i] - pos[i - 1]
            if h[i] > h[i - 1] + d:
                h[i] = h[i - 1] + d
        for i in range(m - 2, -1, -1):
            d = pos[i + 1] - pos[i]
            if h[i] > h[i + 1] + d:
                h[i] = h[i + 1] + d
        max_height = 0
        for i in range(1, m):
            d = pos[i] - pos[i - 1]
            diff = abs(h[i] - h[i - 1])
            peak = max(h[i], h[i - 1]) + (d - diff) // 2
            if peak > max_height:
                max_height = peak
        return max_height