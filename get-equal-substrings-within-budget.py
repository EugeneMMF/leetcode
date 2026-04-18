class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = 0
        cur = 0
        res = 0
        for right in range(n):
            cur += abs(ord(s[right]) - ord(t[right]))
            while cur > maxCost:
                cur -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            if right - left + 1 > res:
                res = right - left + 1
        return res
