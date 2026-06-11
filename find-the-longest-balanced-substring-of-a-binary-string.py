class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            zeros = 0
            ones = 0
            for j in range(i, n):
                if s[j] == '0':
                    if ones > 0:
                        break
                    zeros += 1
                else:
                    ones += 1
                if zeros == ones:
                    ans = max(ans, j - i + 1)
        return ans
