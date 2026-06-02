from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        last = {'M': -1, 'P': -1, 'G': -1}
        count = {'M': 0, 'P': 0, 'G': 0}
        for i, s in enumerate(garbage):
            for c in s:
                count[c] += 1
            for t in 'MPG':
                if t in s:
                    last[t] = i
        prefix = [0] * n
        for i in range(n - 1):
            prefix[i + 1] = prefix[i] + travel[i]
        total = 0
        for t in 'MPG':
            if last[t] != -1:
                total += count[t] + prefix[last[t]]
        return total