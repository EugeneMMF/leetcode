class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        # compute all divisors of n
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1
        divisors.sort()
        for k in divisors:
            # frequency of first segment
            freq = [0] * 26
            for ch in s[:k]:
                freq[ord(ch) - 97] += 1
            ok = True
            for start in range(k, n, k):
                seg_freq = [0] * 26
                for ch in s[start:start + k]:
                    seg_freq[ord(ch) - 97] += 1
                if seg_freq != freq:
                    ok = False
                    break
            if ok:
                return k
        return n
