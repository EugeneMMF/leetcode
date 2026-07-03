class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)
        return len(lower & {c.lower() for c in upper})
