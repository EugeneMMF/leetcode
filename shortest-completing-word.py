import collections

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        lp_chars = [char.lower() for char in licensePlate if char.isalpha()]
        lp_counts = collections.Counter(lp_chars)

        shortest_word = None
        min_length = float('inf')

        for word in words:
            word_counts = collections.Counter(word)
            
            is_completing = True
            for char, count in lp_counts.items():
                if word_counts.get(char, 0) < count:
                    is_completing = False
                    break
            
            if is_completing:
                if len(word) < min_length:
                    min_length = len(word)
                    shortest_word = word
        
        return shortest_word
