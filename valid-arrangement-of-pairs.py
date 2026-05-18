class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        adj = defaultdict(list)
        outdeg = defaultdict(int)
        indeg = defaultdict(int)
        for s, e in pairs:
            adj[s].append((e, [s, e]))
            outdeg[s] += 1
            indeg[e] += 1
        start = None
        for s, e in pairs:
            if outdeg[s] - indeg[s] == 1:
                start = s
                break
        if start is None:
            start = pairs[0][0]
        stack_nodes = [start]
        stack_edges = []
        result = []
        while stack_nodes:
            u = stack_nodes[-1]
            if adj[u]:
                v, edge = adj[u].pop()
                stack_nodes.append(v)
                stack_edges.append(edge)
            else:
                stack_nodes.pop()
                if stack_edges:
                    result.append(stack_edges.pop())
        return result[::-1]