class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        from collections import Counter
        cnt = Counter(s)
        if all(cnt[c] <= target for c in "QWER"):
            return 0
        left = 0
        ans = n
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            while left <= right and all(cnt[c] <= target for c in "QWER"):
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return ans
