class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        res = []
        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters
        for i in range(len(second)):
            res.append(first[i])
            res.append(second[i])
        if len(first) > len(second):
            res.append(first[-1])
        return "".join(res)
