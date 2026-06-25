from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        prev0_len = 1
        prev1_len = 1
        prev0_val = nums1[0]
        prev1_val = nums2[0]
        ans = 1
        for i in range(1, n):
            val0 = nums1[i]
            val1 = nums2[i]
            new0_len = 1
            new1_len = 1
            if val0 >= prev0_val:
                new0_len = max(new0_len, prev0_len + 1)
            if val0 >= prev1_val:
                new0_len = max(new0_len, prev1_len + 1)
            if val1 >= prev0_val:
                new1_len = max(new1_len, prev0_len + 1)
            if val1 >= prev1_val:
                new1_len = max(new1_len, prev1_len + 1)
            ans = max(ans, new0_len, new1_len)
            prev0_len = new0_len
            prev1_len = new1_len
            prev0_val = val0
            prev1_val = val1
        return ans