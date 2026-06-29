class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        if n <= 1:
            return 0
        INF = 10**9
        dp_prev = [INF] * 26
        first_ord = ord(word[0]) - 97
        for c in range(26):
            dp_prev[c] = 0 if c == first_ord else 1
        for i in range(1, n):
            cur_ord = ord(word[i]) - 97
            dp_curr = [INF] * 26
            for c in range(26):
                cost = 0 if c == cur_ord else 1
                best = INF
                for p in range(26):
                    if abs(c - p) > 1:
                        val = dp_prev[p] + cost
                        if val < best:
                            best = val
                dp_curr[c] = best
            dp_prev = dp_curr
        return min(dp_prev)