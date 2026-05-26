class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        parent = [-1] * n
        tin = [0] * n
        tout = [0] * n
        subtree_xor = [0] * n
        timer = 0
        stack = [(0, 0, 0)]
        while stack:
            node, par, state = stack.pop()
            if state == 0:
                parent[node] = par
                tin[node] = timer
                timer += 1
                stack.append((node, par, 1))
                for nei in g[node]:
                    if nei == par:
                        continue
                    stack.append((nei, node, 0))
            else:
                x = nums[node]
                for nei in g[node]:
                    if nei == par:
                        continue
                    x ^= subtree_xor[nei]
                subtree_xor[node] = x
                tout[node] = timer
                timer += 1
        total_xor = subtree_xor[0]
        edge_child = []
        for u, v in edges:
            if parent[u] == v:
                edge_child.append(u)
            else:
                edge_child.append(v)
        m = len(edge_child)
        best = 10**18
        for i in range(m):
            c1 = edge_child[i]
            xor1 = subtree_xor[c1]
            for j in range(i + 1, m):
                c2 = edge_child[j]
                xor2 = subtree_xor[c2]
                if tin[c1] <= tin[c2] <= tout[c1]:
                    a = xor2
                    b = xor1 ^ xor2
                    c = total_xor ^ xor1
                elif tin[c2] <= tin[c1] <= tout[c2]:
                    a = xor1
                    b = xor2 ^ xor1
                    c = total_xor ^ xor2
                else:
                    a = xor1
                    b = xor2
                    c = total_xor ^ xor1 ^ xor2
                mx = max(a, b, c)
                mn = min(a, b, c)
                score = mx - mn
                if score < best:
                    best = score
        return best
