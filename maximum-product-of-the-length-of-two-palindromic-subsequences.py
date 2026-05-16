class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        pal_len = [0] * (1 << n)
        for mask in range(1 << n):
            seq = []
            for i in range(n):
                if mask >> i & 1:
                    seq.append(s[i])
            if seq == seq[::-1]:
                pal_len[mask] = len(seq)
        ans = 0
        for mask1 in range(1 << n):
            if pal_len[mask1] == 0:
                continue
            for mask2 in range(mask1 + 1, 1 << n):
                if pal_len[mask2] == 0:
                    continue
                if mask1 & mask2 == 0:
                    prod = pal_len[mask1] * pal_len[mask2]
                    if prod > ans:
                        ans = prod
        return ans