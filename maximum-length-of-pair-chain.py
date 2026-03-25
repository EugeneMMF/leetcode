import math

class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda p: p[1])

        chain_length = 0
        last_end = -math.inf

        for left, right in pairs:
            if left > last_end:
                chain_length += 1
                last_end = right

        return chain_length
