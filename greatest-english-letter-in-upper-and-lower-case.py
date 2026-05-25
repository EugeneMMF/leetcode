class Solution:
    def greatestLetter(self, s: str) -> str:
        lower=set()
        upper=set()
        for ch in s:
            if 'a' <= ch <= 'z':
                lower.add(ch)
            else:
                upper.add(ch)
        for i in range(ord('Z'), ord('A')-1, -1):
            ch=chr(i)
            if ch.lower() in lower and ch in upper:
                return ch
        return ""
