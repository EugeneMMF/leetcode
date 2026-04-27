class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        if n == 0:
            return 0
        visited = [False] * n
        minDist = [10**9] * n
        minDist[0] = 0
        total = 0
        for _ in range(n):
            u = -1
            best = 10**9
            for i in range(n):
                if not visited[i] and minDist[i] < best:
                    best = minDist[i]
                    u = i
            visited[u] = True
            total += best
            xu, yu = points[u]
            for v in range(n):
                if not visited[v]:
                    d = abs(xu - points[v][0]) + abs(yu - points[v][1])
                    if d < minDist[v]:
                        minDist[v] = d
        return total
