class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        import sys
        sys.setrecursionlimit(200000)
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        coprime = [[] for _ in range(51)]
        for a in range(1, 51):
            for b in range(1, 51):
                if __import__('math').gcd(a, b) == 1:
                    coprime[a].append(b)
        last = [-1] * 51
        depth = [0] * n
        ans = [-1] * n
        def dfs(u, p, d):
            best = -1
            bestd = -1
            val = nums[u]
            for cv in coprime[val]:
                anc = last[cv]
                if anc != -1 and depth[anc] > bestd:
                    bestd = depth[anc]
                    best = anc
            ans[u] = best
            prev = last[val]
            last[val] = u
            depth[u] = d
            for v in g[u]:
                if v != p:
                    dfs(v, u, d + 1)
            last[val] = prev
        dfs(0, -1, 0)
        return ans
