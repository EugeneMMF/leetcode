import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        
        projects = []
        for i in range(n):
            projects.append((capital[i], profits[i]))
        
        projects.sort()
        
        available_profits = []
        
        project_idx = 0
        
        for _ in range(k):
            while project_idx < n and projects[project_idx][0] <= w:
                heapq.heappush(available_profits, -projects[project_idx][1])
                project_idx += 1
            
            if not available_profits:
                break
            
            max_profit = -heapq.heappop(available_profits)
            
            w += max_profit
            
        return w
