class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        from collections import defaultdict
        deg = [0] * (n + 1)
        pair_cnt = defaultdict(int)
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            pair_cnt[(u, v)] += 1
        sorted_deg = sorted(deg[1:])
        answers = []
        for k in queries:
            cnt = 0
            l, r = 0, n - 1
            while l < r:
                if sorted_deg[l] + sorted_deg[r] > k:
                    cnt += r - l
                    r -= 1
                else:
                    l += 1
            for (u, v), c in pair_cnt.items():
                s = deg[u] + deg[v]
                if s > k and s - c <= k:
                    cnt -= 1
            answers.append(cnt)
        return answers
