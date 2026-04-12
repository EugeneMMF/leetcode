class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        from heapq import heappush, heappop
        def heuristic(a):
            diff = sum(1 for i in range(len(a)) if a[i] != s2[i])
            return (diff + 1) // 2
        start = s1
        visited = {start: 0}
        heap = []
        heappush(heap, (heuristic(start), 0, start))
        while heap:
            f, g, cur = heappop(heap)
            if cur == s2:
                return g
            if visited.get(cur, 1 << 30) < g:
                continue
            i = 0
            n = len(cur)
            while i < n and cur[i] == s2[i]:
                i += 1
            cur_list = list(cur)
            for j in range(i + 1, n):
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
                    nxt = ''.join(cur_list)
                    if visited.get(nxt, 1 << 30) > g + 1:
                        visited[nxt] = g + 1
                        heappush(heap, (g + 1 + heuristic(nxt), g + 1, nxt))
                    cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
            # If no beneficial swap found, try generic swaps that match target[i]
            if not any(cur[j] == s2[i] and cur[j] != s2[j] for j in range(i + 1, n)):
                for j in range(i + 1, n):
                    if cur[j] == s2[i]:
                        cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
                        nxt = ''.join(cur_list)
                        if visited.get(nxt, 1 << 30) > g + 1:
                            visited[nxt] = g + 1
                            heappush(heap, (g + 1 + heuristic(nxt), g + 1, nxt))
                        cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
