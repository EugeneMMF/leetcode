class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        vowels = set('aeiou')
        max_vowel = 0
        max_consonant = 0
        for ch, cnt in counts.items():
            if ch in vowels:
                if cnt > max_vowel:
                    max_vowel = cnt
            else:
                if cnt > max_consonant:
                    max_consonant = cnt
        return max_vowel + max_consonant
