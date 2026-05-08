class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        total = 0
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                total = (total + count * (count + 1) // 2) % mod
                count = 1
        total = (total + count * (count + 1) // 2) % mod
        return total