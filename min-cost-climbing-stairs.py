
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        
        cost_to_reach_prev_prev = 0
        cost_to_reach_prev = 0
        
        for i in range(2, n + 1):
            current_cost = min(cost_to_reach_prev + cost[i-1], cost_to_reach_prev_prev + cost[i-2])
            cost_to_reach_prev_prev = cost_to_reach_prev
            cost_to_reach_prev = current_cost
            
        return cost_to_reach_prev
