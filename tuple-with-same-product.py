class Solution:
    def tupleSameProduct(self, nums):
        n = len(nums)
        prod_map = {}
        for i in range(n):
            ai = nums[i]
            for j in range(i + 1, n):
                p = ai * nums[j]
                prod_map.setdefault(p, []).append((i, j))
        ans = 0
        for pairs in prod_map.values():
            m = len(pairs)
            if m < 2:
                continue
            for x in range(m):
                i1, j1 = pairs[x]
                for y in range(x + 1, m):
                    i2, j2 = pairs[y]
                    if i1 != i2 and i1 != j2 and j1 != i2 and j1 != j2:
                        ans += 8
        return ans
