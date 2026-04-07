import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        adj = collections.defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)

        max_total_time = 0
        q = collections.deque([(headID, 0)])

        while q:
            curr_employee, time_to_reach_curr = q.popleft()
            max_total_time = max(max_total_time, time_to_reach_curr)
            
            for subordinate in adj[curr_employee]:
                q.append((subordinate, time_to_reach_curr + informTime[curr_employee]))
        
        return max_total_time
