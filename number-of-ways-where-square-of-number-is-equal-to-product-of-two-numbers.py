from typing import List

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(a, b):
            prod = {}
            n = len(b)
            for i in range(n):
                bi = b[i]
                for j in range(i + 1, n):
                    p = bi * b[j]
                    prod[p] = prod.get(p, 0) + 1
            total = 0
            for x in a:
                total += prod.get(x * x, 0)
            return total
        return count(nums1, nums2) + count(nums2, nums1)
