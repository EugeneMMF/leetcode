import collections

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        sorted_deck = sorted(deck)
        result = [0] * n
        indices_queue = collections.deque(range(n))
        
        for card in sorted_deck:
            reveal_position = indices_queue.popleft()
            result[reveal_position] = card
            
            if indices_queue:
                next_card_position = indices_queue.popleft()
                indices_queue.append(next_card_position)
                
        return result
