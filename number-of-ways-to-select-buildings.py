class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        total0 = s.count('0')
        total1 = n - total0
        left0 = left1 = 0
        ans = 0
        for j, ch in enumerate(s):
            if ch == '0':
                left1 = j - left0
                right1 = total1 - left1
                ans += left1 * right1
                left0 += 1
            else:
                left0 = j - left1
                right0 = total0 - left0
                ans += left0 * right0
                left1 += 1
        return ans