class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        next0 = [-1] * (n + 1)
        next1 = [-1] * (n + 1)
        next0[n] = -1
        next1[n] = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                next0[i] = i
                next1[i] = next1[i + 1]
            else:
                next1[i] = i
                next0[i] = next0[i + 1]
        def feasible(L: int) -> bool:
            pos = 0
            subseq = []
            for i in range(L):
                idx = next0[pos] if pos <= n else -1
                if idx != -1 and n - idx >= L - i:
                    subseq.append('0')
                    pos = idx + 1
                else:
                    idx = next1[pos] if pos <= n else -1
                    if idx != -1 and n - idx >= L - i:
                        subseq.append('1')
                        pos = idx + 1
                    else:
                        return False
            val = 0
            for c in subseq:
                val = (val << 1) + (c == '1')
                if val > k:
                    return False
            return True
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo