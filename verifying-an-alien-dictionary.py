from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            j = 0
            while j < len(w1) and j < len(w2) and w1[j] == w2[j]:
                j += 1
            if j == len(w2) and j < len(w1):
                return False
            if j < len(w1) and j < len(w2):
                if rank[w1[j]] > rank[w2[j]]:
                    return False
        return True
