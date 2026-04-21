class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)
        pi = [0] * m
        for i in range(1, m):
            j = pi[i-1]
            while j > 0 and evil[i] != evil[j]:
                j = pi[j-1]
            if evil[i] == evil[j]:
                j += 1
            pi[i] = j
        trans = [[0]*26 for _ in range(m+1)]
        for state in range(m+1):
            for ch in range(26):
                if state == m:
                    trans[state][ch] = m
                    continue
                c = chr(ord('a') + ch)
                j = state
                while j > 0 and evil[j] != c:
                    j = pi[j-1]
                if evil[j] == c:
                    j += 1
                trans[state][ch] = j
        dp = [[[[0]*2 for _ in range(2)] for __ in range(m)] for ___ in range(n+1)]
        dp[0][0][1][1] = 1
        for i in range(n):
            for st in range(m):
                for lo in range(2):
                    for hi in range(2):
                        cur = dp[i][st][lo][hi]
                        if not cur:
                            continue
                        low = ord(s1[i]) - 97 if lo else 0
                        high = ord(s2[i]) - 97 if hi else 25
                        for ch in range(low, high+1):
                            nlo = lo and (ch == low and lo) and (ch == ord(s1[i]) - 97)
                            nhi = hi and (ch == high and hi) and (ch == ord(s2[i]) - 97)
                            nlo = lo and (ch == low) and (ch == ord(s1[i]) - 97)
                            nhi = hi and (ch == high) and (ch == ord(s2[i]) - 97)
                            nst = trans[st][ch]
                            if nst == m:
                                continue
                            dp[i+1][nst][nlo][nhi] = (dp[i+1][nst][nlo][nhi] + cur) % MOD
        ans = 0
        for st in range(m):
            for lo in range(2):
                for hi in range(2):
                    ans = (ans + dp[n][st][lo][hi]) % MOD
        return ans
