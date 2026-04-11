from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        prev = -10**9
        for i, ch in enumerate(s):
            if ch == c:
                prev = i
            ans[i] = i - prev
        prev = 10**9
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans
