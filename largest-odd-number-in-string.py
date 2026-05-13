class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_odd = -1
        for i, ch in enumerate(num):
            if int(ch) % 2 == 1:
                last_odd = i
        if last_odd == -1:
            return ""
        return num[:last_odd + 1]
