from collections import Counter
import math
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        g = 0
        for c in cnt.values():
            g = math.gcd(g, c)
        return g > 1
