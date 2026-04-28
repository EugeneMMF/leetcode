class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        ans = 0
        for i in range(n):
            for j in range(m):
                mism = 0
                k = 0
                while i + k < n and j + k < m:
                    if s[i + k] != t[j + k]:
                        mism += 1
                    if mism == 1:
                        ans += 1
                    elif mism > 1:
                        break
                    k += 1
        return ans
