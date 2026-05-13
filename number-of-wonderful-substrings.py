class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = [0] * 1024
        mask = 0
        freq[mask] = 1
        count = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - 97)
            count += freq[mask]
            for i in range(10):
                count += freq[mask ^ (1 << i)]
            freq[mask] += 1
        return count
