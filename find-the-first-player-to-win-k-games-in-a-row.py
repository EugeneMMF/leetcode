from typing import List
from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        max_skill = max(skills)
        if k >= n - 1:
            return skills.index(max_skill)
        dq = deque(range(n))
        a = dq.popleft()
        b = dq.popleft()
        if skills[a] > skills[b]:
            winner = a
            loser = b
        else:
            winner = b
            loser = a
        win_count = 1
        dq.appendleft(winner)
        dq.append(loser)
        while win_count < k:
            a = dq.popleft()
            b = dq.popleft()
            if skills[a] > skills[b]:
                new_winner = a
                new_loser = b
            else:
                new_winner = b
                new_loser = a
            if new_winner == winner:
                win_count += 1
            else:
                winner = new_winner
                win_count = 1
            dq.appendleft(new_winner)
            dq.append(new_loser)
        return winner
