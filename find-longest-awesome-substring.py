class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        earliest = {0: -1}
        ans = 0
        for i, ch in enumerate(s):
            mask ^= 1 << (ord(ch) - 48)
            if mask in earliest:
                ans = max(ans, i - earliest[mask])
            else:
                earliest[mask] = i
            for b in range(10):
                m2 = mask ^ (1 << b)
                if m2 in earliest:
                    ans = max(ans, i - earliest[m2])
        return ans
