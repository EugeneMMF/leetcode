class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(1 << 25)
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        best_len = 0
        best_nodes = 1
        path_nodes = []
        dist_path = []
        value_to_pos = {}
        def dfs(node: int, parent: int, dist: int, start: int):
            nonlocal best_len, best_nodes
            path_nodes.append(node)
            dist_path.append(dist)
            val = nums[node]
            prev_pos = value_to_pos.get(val, -1)
            if prev_pos >= start:
                start = prev_pos + 1
            old_val = value_to_pos.get(val)
            value_to_pos[val] = len(path_nodes) - 1
            cur_len = dist - dist_path[start]
            cur_nodes = len(path_nodes) - start
            if cur_len > best_len or (cur_len == best_len and cur_nodes < best_nodes):
                best_len = cur_len
                best_nodes = cur_nodes
            for nxt, w in adj[node]:
                if nxt == parent:
                    continue
                dfs(nxt, node, dist + w, start)
            # backtrack
            path_nodes.pop()
            dist_path.pop()
            if old_val is None:
                del value_to_pos[val]
            else:
                value_to_pos[val] = old_val
        dfs(0, -1, 0, 0)
        return [best_len, best_nodes]
