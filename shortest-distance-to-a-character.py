class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        ans = [0] * n

        prev_c_idx = -n
        for i in range(n):
            if s[i] == c:
                prev_c_idx = i
            ans[i] = i - prev_c_idx

        next_c_idx = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_c_idx = i
            ans[i] = min(ans[i], next_c_idx - i)
            
        return ans

