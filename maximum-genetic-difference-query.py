class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        adj = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                adj[p].append(i)
        qn = len(queries)
        ans = [0] * qn
        queries_by_node = [[] for _ in range(n)]
        for idx, (node, val) in enumerate(queries):
            queries_by_node[node].append((val, idx))
        maxbit = 18
        trie = [[-1, -1, 0]]
        def insert(x):
            node = 0
            trie[node][2] += 1
            for b in range(maxbit - 1, -1, -1):
                bit = (x >> b) & 1
                nxt = trie[node][bit]
                if nxt == -1:
                    nxt = len(trie)
                    trie[node][bit] = nxt
                    trie.append([-1, -1, 0])
                node = nxt
                trie[node][2] += 1
        def delete(x):
            node = 0
            trie[node][2] -= 1
            for b in range(maxbit - 1, -1, -1):
                bit = (x >> b) & 1
                node = trie[node][bit]
                trie[node][2] -= 1
        def query(x):
            node = 0
            res = 0
            for b in range(maxbit - 1, -1, -1):
                bit = (x >> b) & 1
                pref = bit ^ 1
                if trie[node][pref] != -1 and trie[trie[node][pref]][2] > 0:
                    res |= (1 << b)
                    node = trie[node][pref]
                else:
                    node = trie[node][bit]
            return res
        import sys
        sys.setrecursionlimit(300000)
        def dfs(u):
            insert(u)
            for val, idx in queries_by_node[u]:
                ans[idx] = query(val)
            for v in adj[u]:
                dfs(v)
            delete(u)
        dfs(root)
        return ans