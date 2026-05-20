class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i
        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 2)
            def add(self, i, v):
                while i <= self.n:
                    self.bit[i] += v
                    i += i & -i
            def sum(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s
        bit_seen = BIT(n)
        bit_remain = BIT(n)
        for i in range(1, n + 1):
            bit_remain.add(i, 1)
        ans = 0
        for val in nums1:
            p = pos2[val] + 1
            left_smaller = bit_seen.sum(p - 1)
            right_greater = bit_remain.sum(n) - bit_remain.sum(p)
            ans += left_smaller * right_greater
            bit_seen.add(p, 1)
            bit_remain.add(p, -1)
        return ans
