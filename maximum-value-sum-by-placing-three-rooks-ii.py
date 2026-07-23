class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        import heapq
        m = len(board)
        n = len(board[0])
        s = 0
        t = m + n + 1
        N = m + n + 2
        graph = [[] for _ in range(N)]
        def add_edge(u, v, cap, cost):
            graph[u].append([v, len(graph[v]), cap, cost])
            graph[v].append([u, len(graph[u]) - 1, 0, -cost])
        for i in range(m):
            add_edge(s, 1 + i, 1, 0)
        for j in range(n):
            add_edge(1 + m + j, t, 1, 0)
        for i in range(m):
            row = board[i]
            u = 1 + i
            for j in range(n):
                v = 1 + m + j
                add_edge(u, v, 1, -row[j])
        INF = 10**30
        potential = [0] * N
        dist = [0] * N
        prevv = [0] * N
        preve = [0] * N
        flow = 0
        cost = 0
        while flow < 3:
            for i in range(N):
                dist[i] = INF
            dist[s] = 0
            hq = [(0, s)]
            while hq:
                d, v = heapq.heappop(hq)
                if d != dist[v]:
                    continue
                for ei, e in enumerate(graph[v]):
                    to, rev, cap, ecost = e
                    if cap > 0:
                        nd = d + ecost + potential[v] - potential[to]
                        if nd < dist[to]:
                            dist[to] = nd
                            prevv[to] = v
                            preve[to] = ei
                            heapq.heappush(hq, (nd, to))
            if dist[t] == INF:
                break
            for v in range(N):
                if dist[v] < INF:
                    potential[v] += dist[v]
            addf = 1
            v = t
            path_cost = 0
            while v != s:
                pv = prevv[v]
                ei = preve[v]
                e = graph[pv][ei]
                path_cost += e[3]
                e[2] -= addf
                graph[v][e[1]][2] += addf
                v = pv
            flow += addf
            cost += path_cost * addf
        return -cost
