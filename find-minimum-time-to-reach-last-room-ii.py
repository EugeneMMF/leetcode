class Solution:
    def minTimeToReach(self, moveTime):
        import heapq
        n = len(moveTime)
        m = len(moveTime[0])
        INF = 10**20
        dist = [[[INF, INF] for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0
        heap = [(0, 0, 0, 0)]
        while heap:
            t, i, j, p = heapq.heappop(heap)
            if t != dist[i][j][p]:
                continue
            if i == n - 1 and j == m - 1:
                continue
            cost = 1 if p == 0 else 2
            np = 1 - p
            if i > 0:
                ni, nj = i - 1, j
                start = t if t >= moveTime[ni][nj] else moveTime[ni][nj]
                nt = start + cost
                if nt < dist[ni][nj][np]:
                    dist[ni][nj][np] = nt
                    heapq.heappush(heap, (nt, ni, nj, np))
            if i < n - 1:
                ni, nj = i + 1, j
                start = t if t >= moveTime[ni][nj] else moveTime[ni][nj]
                nt = start + cost
                if nt < dist[ni][nj][np]:
                    dist[ni][nj][np] = nt
                    heapq.heappush(heap, (nt, ni, nj, np))
            if j > 0:
                ni, nj = i, j - 1
                start = t if t >= moveTime[ni][nj] else moveTime[ni][nj]
                nt = start + cost
                if nt < dist[ni][nj][np]:
                    dist[ni][nj][np] = nt
                    heapq.heappush(heap, (nt, ni, nj, np))
            if j < m - 1:
                ni, nj = i, j + 1
                start = t if t >= moveTime[ni][nj] else moveTime[ni][nj]
                nt = start + cost
                if nt < dist[ni][nj][np]:
                    dist[ni][nj][np] = nt
                    heapq.heappush(heap, (nt, ni, nj, np))
        return min(dist[n - 1][m - 1][0], dist[n - 1][m - 1][1])