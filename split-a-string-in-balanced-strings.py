class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = ans = 0
        for ch in s:
            cnt += 1 if ch == 'R' else -1
            if cnt == 0:
                ans += 1
        return ans
