import bisect

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        heights = [envelope[1] for envelope in envelopes]

        tails = []
        for height in heights:
            idx = bisect.bisect_left(tails, height)
            if idx == len(tails):
                tails.append(height)
            else:
                tails[idx] = height
        
        return len(tails)
