class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        nums = []
        from itertools import permutations
        for mask in range(1, 1 << 9):
            digits = []
            total = 0
            for d in range(1, 10):
                if mask & (1 << (d - 1)):
                    digits.extend([d] * d)
                    total += d
            if total > 7:
                continue
            seen = set()
            for p in permutations(digits):
                if p[0] == 0:
                    continue
                val = 0
                for x in p:
                    val = val * 10 + x
                if val not in seen:
                    seen.add(val)
                    nums.append(val)
        nums = sorted(set(nums))
        for x in nums:
            if x > n:
                return x
        return -1