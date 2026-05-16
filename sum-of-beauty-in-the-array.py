class Solution:
    def sumOfBeauties(self, nums):
        n = len(nums)
        prefix_max = [0]*n
        suffix_min = [0]*n
        cur_max = -1
        for i in range(n):
            prefix_max[i] = cur_max
            if nums[i] > cur_max:
                cur_max = nums[i]
        cur_min = 10**6+1
        for i in range(n-1, -1, -1):
            suffix_min[i] = cur_min
            if nums[i] < cur_min:
                cur_min = nums[i]
        total = 0
        for i in range(1, n-1):
            if prefix_max[i] < nums[i] < suffix_min[i]:
                total += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                total += 1
        return total