class Solution:
    def missingInteger(self, nums):
        longest_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_sum += nums[i]
                if current_sum > longest_sum:
                    longest_sum = current_sum
            else:
                break
        nums_set = set(nums)
        candidate = longest_sum
        while candidate in nums_set:
            candidate += 1
        return candidate
