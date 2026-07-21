class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        ans = 0
        for c in cnt:
            if c:
                ans += 2 if c % 2 == 0 else 1
        return ans