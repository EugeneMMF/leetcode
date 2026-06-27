class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        max_alloys = 0
        for i in range(k):
            low, high = 0, 2000000000
            best = 0
            while low <= high:
                mid = (low + high) // 2
                total_cost = 0
                for j in range(n):
                    need = composition[i][j] * mid - stock[j]
                    if need > 0:
                        total_cost += need * cost[j]
                        if total_cost > budget:
                            break
                if total_cost <= budget:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1
            if best > max_alloys:
                max_alloys = best
        return max_alloys