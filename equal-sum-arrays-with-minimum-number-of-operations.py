class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 < sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1
        diff = sum1 - sum2
        counts1 = [0] * 7
        counts2 = [0] * 7
        for v in nums1:
            counts1[v] += 1
        for v in nums2:
            counts2[v] += 1
        change_counts = [0] * 6
        for v in range(2, 7):
            change = v - 1
            change_counts[change] += counts1[v]
        for v in range(1, 6):
            change = 6 - v
            change_counts[change] += counts2[v]
        ops = 0
        for change in range(5, 0, -1):
            if diff <= 0:
                break
            available = change_counts[change]
            if available == 0:
                continue
            max_use = (diff + change - 1) // change
            use = min(available, max_use)
            diff -= use * change
            ops += use
        return ops if diff <= 0 else -1
