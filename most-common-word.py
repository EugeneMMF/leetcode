from typing import List
import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"\w+", paragraph.lower())
        banned_set = set(banned)
        freq = collections.Counter(w for w in words if w not in banned_set)
        return max(freq, key=freq.get)
