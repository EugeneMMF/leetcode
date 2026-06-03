class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter
        freq = Counter(word)
        for ch in word:
            new_freq = freq.copy()
            new_freq[ch] -= 1
            if new_freq[ch] == 0:
                del new_freq[ch]
            if len(set(new_freq.values())) == 1:
                return True
        return False