class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def val(s):
            return int(''.join(str(ord(c)-97) for c in s))
        return val(firstWord) + val(secondWord) == val(targetWord)
