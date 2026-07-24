class Solution:
    def minOperations(self, n: int, m: int) -> int:
        import heapq
        max_val = 10000
        is_prime = [True] * max_val
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val ** 0.5) + 1):
            if is_prime[i]:
                step = i
                start = i * i
                for j in range(start, max_val, step):
                    is_prime[j] = False
        if is_prime[n] or is_prime[m]:
            return -1
        L = len(str(n))
        dist = [float('inf')] * max_val
        dist[n] = n
        heap = [(n, n)]
        while heap:
            cost, node = heapq.heappop(heap)
            if cost != dist[node]:
                continue
            if node == m:
                return cost
            s = str(node).zfill(L)
            for i in range(L):
                d = int(s[i])
                if d < 9:
                    ns = s[:i] + str(d + 1) + s[i+1:]
                    v = int(ns)
                    if not is_prime[v]:
                        new_cost = cost + v
                        if new_cost < dist[v]:
                            dist[v] = new_cost
                            heapq.heappush(heap, (new_cost, v))
                if d > 0:
                    if i == 0 and d == 1:
                        continue
                    ns = s[:i] + str(d - 1) + s[i+1:]
                    v = int(ns)
                    if not is_prime[v]:
                        new_cost = cost + v
                        if new_cost < dist[v]:
                            dist[v] = new_cost
                            heapq.heappush(heap, (new_cost, v))
        return -1