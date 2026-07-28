from typing import List

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = {}
        for day in responses:
            seen = set(day)
            for r in seen:
                freq[r] = freq.get(r, 0) + 1
        best_word = None
        best_count = -1
        for word, count in freq.items():
            if count > best_count or (count == best_count and word < best_word):
                best_count = count
                best_word = word
        return best_word