class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        m = len(factory)
        N = 2 + n + m
        g = [[] for _ in range(N)]
        def add_edge(fr, to, cap, cost):
            g[fr].append([to, cap, cost, len(g[to])])
            g[to].append([fr, 0, -cost, len(g[fr]) - 1])
        S = 0
        T = N - 1
        for i, r in enumerate(robot):
            add_edge(S, 1 + i, 1, 0)
        for j, (p, lim) in enumerate(factory):
            add_edge(1 + n + j, T, lim, 0)
        for i, r in enumerate(robot):
            for j, (p, _) in enumerate(factory):
                add_edge(1 + i, 1 + n + j, 1, abs(r - p))
        flow = 0
        cost = 0
        INF = 10**18
        potential = [0] * N
        dist = [0] * N
        prevv = [0] * N
        preve = [0] * N
        while flow < n:
            import heapq
            for i in range(N):
                dist[i] = INF
            dist[S] = 0
            hq = [(0, S)]
            while hq:
                d, v = heapq.heappop(hq)
                if dist[v] < d:
                    continue
                for i, e in enumerate(g[v]):
                    to, cap, cost_e, rev = e
                    if cap > 0 and dist[to] > dist[v] + cost_e + potential[v] - potential[to]:
                        dist[to] = dist[v] + cost_e + potential[v] - potential[to]
                        prevv[to] = v
                        preve[to] = i
                        heapq.heappush(hq, (dist[to], to))
            if dist[T] == INF:
                return 0
            for v in range(N):
                if dist[v] < INF:
                    potential[v] += dist[v]
            d = n - flow
            v = T
            while v != S:
                d = min(d, g[prevv[v]][preve[v]][1])
                v = prevv[v]
            flow += d
            cost += d * potential[T]
            v = T
            while v != S:
                e = g[prevv[v]][preve[v]]
                e[1] -= d
                g[v][e[3]][1] += d
                v = prevv[v]
        return cost