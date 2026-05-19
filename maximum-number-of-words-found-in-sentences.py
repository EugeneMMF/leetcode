from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for s in sentences:
            words = s.split(' ')
            if len(words) > max_words:
                max_words = len(words)
        return max_words
