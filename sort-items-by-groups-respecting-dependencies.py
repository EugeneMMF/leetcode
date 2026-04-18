class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        new_group = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group
                new_group += 1
        total_groups = new_group
        item_adj = [[] for _ in range(n)]
        item_indeg = [0] * n
        group_adj = [[] for _ in range(total_groups)]
        group_indeg = [0] * total_groups
        for i in range(n):
            for pre in beforeItems[i]:
                if group[pre] == group[i]:
                    item_adj[pre].append(i)
                    item_indeg[i] += 1
                else:
                    group_adj[group[pre]].append(group[i])
                    group_indeg[group[i]] += 1
        def topo(nodes, adj, indeg):
            q = [i for i in nodes if indeg[i] == 0]
            res = []
            for u in q:
                res.append(u)
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            return res if len(res) == len(nodes) else []
        group_order = topo(list(range(total_groups)), group_adj, group_indeg[:])
        if not group_order:
            return []
        item_order = topo(list(range(n)), item_adj, item_indeg[:])
        if not item_order:
            return []
        group_items = [[] for _ in range(total_groups)]
        for item in item_order:
            group_items[group[item]].append(item)
        res = []
        for g in group_order:
            res.extend(group_items[g])
        return res
