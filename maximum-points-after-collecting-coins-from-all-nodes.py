class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        H = 15
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = -2
        while stack:
            v = stack.pop()
            order.append(v)
            for nei in adj[v]:
                if parent[nei] == -1:
                    parent[nei] = v
                    stack.append(nei)
        dp = [[0] * (H + 2) for _ in range(n)]
        for v in reversed(order):
            child_dp_lists = []
            for nei in adj[v]:
                if nei == parent[v]:
                    continue
                child_dp_lists.append(dp[nei])
            coin_halved = [coins[v] >> h for h in range(H + 1)]
            for h in range(H, -1, -1):
                coin = coin_halved[h]
                opt1 = coin - k
                opt2 = coin // 2
                sum1 = 0
                sum2 = 0
                for ch_dp in child_dp_lists:
                    sum1 += ch_dp[h]
                    sum2 += ch_dp[h + 1]
                dp[v][h] = opt1 + sum1 if opt1 + sum1 > opt2 + sum2 else opt2 + sum2
        return dp[0][0]
