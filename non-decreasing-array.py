class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        n = len(nums)
        violations = 0

        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                violations += 1
                if violations > 1:
                    return False
                
                # To fix the violation nums[i] > nums[i+1], we have two choices:
                # 1. Decrease nums[i] to nums[i+1]
                # 2. Increase nums[i+1] to nums[i]

                # We prefer to decrease nums[i] because it usually causes less disruption
                # to the subsequent sequence. This is valid if:
                # a) i is the first element (no element before nums[i] to worry about)
                # b) nums[i-1] <= nums[i+1] (decreasing nums[i] won't create a new violation with nums[i-1])
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                # If we cannot decrease nums[i] (because nums[i-1] > nums[i+1]),
                # then we must increase nums[i+1] to nums[i].
                # This might create a new violation with nums[i+2], but that will
                # be caught by the violations counter in the next iteration.
                else:
                    nums[i+1] = nums[i]
        
        return True
