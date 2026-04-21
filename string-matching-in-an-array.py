from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, w in enumerate(words):
            for j, other in enumerate(words):
                if i != j and w in other:
                    result.append(w)
                    break
        return result
