class Solution:
    def largestCombination(self, candidates):
        counts = [0] * 32
        for num in candidates:
            for b in range(32):
                if num >> b & 1:
                    counts[b] += 1
        return max(counts)
