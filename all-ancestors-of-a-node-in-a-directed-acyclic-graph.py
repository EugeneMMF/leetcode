class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import deque
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        ancestors = [0] * n
        q = deque([i for i in range(n) if indegree[i] == 0])
        while q:
            u = q.popleft()
            for v in graph[u]:
                ancestors[v] |= ancestors[u] | (1 << u)
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        answer = []
        for i in range(n):
            anc = ancestors[i]
            res = []
            j = 0
            while anc:
                if anc & 1:
                    res.append(j)
                anc >>= 1
                j += 1
            answer.append(res)
        return answer