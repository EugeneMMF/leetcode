class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp_prev = [0] * n
        # Day 0
        dp_cur = [0] * n
        for c in range(n):
            max_travel = 0
            for s in range(n):
                val = travelScore[s][c]
                if val > max_travel:
                    max_travel = val
            dp_cur[c] = max(stayScore[0][c], max_travel)
        dp_prev = dp_cur
        for day in range(1, k):
            dp_cur = [0] * n
            for c in range(n):
                stay_val = dp_prev[c] + stayScore[day][c]
                move_val = 0
                for p in range(n):
                    val = dp_prev[p] + travelScore[p][c]
                    if val > move_val:
                        move_val = val
                dp_cur[c] = stay_val if stay_val > move_val else move_val
            dp_prev = dp_cur
        return max(dp_prev)