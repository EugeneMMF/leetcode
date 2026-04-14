class Solution:
    def deckRevealedIncreasing(self, deck):
        from collections import deque
        deck.sort()
        dq = deque()
        for card in reversed(deck):
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(card)
        return list(dq)
