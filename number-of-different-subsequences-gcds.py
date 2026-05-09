class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        from math import gcd
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
        g = [0] * (max_val + 1)
        for v in range(1, max_val + 1):
            cur_gcd = 0
            for m in range(v, max_val + 1, v):
                if freq[m]:
                    cur_gcd = gcd(cur_gcd, m)
                    if cur_gcd == v:
                        break
            g[v] = cur_gcd
        return sum(1 for v in range(1, max_val + 1) if g[v] == v)