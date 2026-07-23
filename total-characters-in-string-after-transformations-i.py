class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 1000000007
        cur = [1] * 26
        for _ in range(t):
            nxt = [0] * 26
            nxt[25] = (cur[0] + cur[1]) % mod
            for i in range(25):
                nxt[i] = cur[i + 1]
            cur = nxt
        total = 0
        for ch in s:
            total = (total + cur[ord(ch) - 97]) % mod
        return total