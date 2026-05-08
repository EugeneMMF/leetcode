class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        m = len(toppingCosts)
        sums = []
        def dfs(i, curr):
            if i == m:
                sums.append(curr)
                return
            for k in range(3):
                dfs(i + 1, curr + k * toppingCosts[i])
        dfs(0, 0)
        best = None
        bestDiff = None
        for base in baseCosts:
            for s in sums:
                total = base + s
                diff = abs(total - target)
                if best is None or diff < bestDiff or (diff == bestDiff and total < best):
                    best = total
                    bestDiff = diff
        return best