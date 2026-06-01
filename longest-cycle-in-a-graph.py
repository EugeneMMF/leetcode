class Solution:
    def longestCycle(self, edges):
        n = len(edges)
        visited = [0] * n
        depth = [0] * n
        ans = -1
        for i in range(n):
            if visited[i]:
                continue
            cur = i
            step = 0
            stack = {}
            while cur != -1 and not visited[cur]:
                visited[cur] = 1
                depth[cur] = step
                stack[cur] = step
                cur = edges[cur]
                step += 1
            if cur != -1 and visited[cur] == 1:
                cycle_len = step - depth[cur]
                if cycle_len > ans:
                    ans = cycle_len
            for node in stack:
                visited[node] = 2
        return ans if ans != -1 else -1