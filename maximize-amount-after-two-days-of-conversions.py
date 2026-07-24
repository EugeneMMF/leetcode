class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        from collections import defaultdict
        adj1 = defaultdict(list)
        for (a, b), r in zip(pairs1, rates1):
            adj1[a].append((b, r))
            adj1[b].append((a, 1 / r))
        adj2 = defaultdict(list)
        for (a, b), r in zip(pairs2, rates2):
            adj2[a].append((b, r))
            adj2[b].append((a, 1 / r))
        def compute(adj):
            rates = {}
            stack = [(initialCurrency, 1.0)]
            visited = set()
            while stack:
                node, val = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                rates[node] = val
                for nb, rate in adj[node]:
                    if nb not in visited:
                        stack.append((nb, val * rate))
            return rates
        rates_day1 = compute(adj1)
        rates_day2 = compute(adj2)
        best = 0.0
        for cur in rates_day1:
            if cur in rates_day2:
                amt = rates_day1[cur] * (1.0 / rates_day2[cur])
                if amt > best:
                    best = amt
        return best
