class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - 97] += 1
        n = len(word)
        maxfreq = max(freq)
        best = 0
        for m in range(1, maxfreq + 1):
            total = 0
            limit = m + k
            for f in freq:
                if f >= m:
                    total += f if f <= limit else limit
            if total > best:
                best = total
        return n - best
