class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        m = n // k
        freq = {}
        for i in range(0, n, k):
            block = word[i:i+k]
            freq[block] = freq.get(block, 0) + 1
        maxfreq = max(freq.values())
        return m - maxfreq