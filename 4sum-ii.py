from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count_ab = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                count_ab[n1 + n2] += 1
        
        total_tuples = 0
        for n3 in nums3:
            for n4 in nums4:
                target_sum_for_ab = -(n3 + n4)
                if target_sum_for_ab in count_ab:
                    total_tuples += count_ab[target_sum_for_ab]
        
        return total_tuples
