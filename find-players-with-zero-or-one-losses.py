from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        all_players = set()
        for w, l in matches:
            all_players.add(w)
            all_players.add(l)
            loss_count[l] = loss_count.get(l, 0) + 1
        winners = []
        one_loss = []
        for p in all_players:
            cnt = loss_count.get(p, 0)
            if cnt == 0:
                winners.append(p)
            elif cnt == 1:
                one_loss.append(p)
        winners.sort()
        one_loss.sort()
        return [winners, one_loss]
