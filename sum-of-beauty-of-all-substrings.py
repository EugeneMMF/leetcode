class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                idx = ord(s[j]) - 97
                freq[idx] += 1
                maxf = 0
                minf = n + 1
                for f in freq:
                    if f:
                        if f > maxf:
                            maxf = f
                        if f < minf:
                            minf = f
                if maxf > minf:
                    total += maxf - minf
        return total
