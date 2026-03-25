class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # The maximum product can come from two scenarios:
        # 1. Product of the three largest numbers (e.g., [1,2,3,4] -> 4*3*2 = 24)
        # 2. Product of the two smallest (most negative) numbers and the largest number
        #    (e.g., [-100, -2, -1, 1, 2, 3] -> (-100)*(-2)*3 = 600)
        
        product_of_three_largest = nums[n-1] * nums[n-2] * nums[n-3]
        product_of_two_smallest_and_largest = nums[0] * nums[1] * nums[n-1]
        
        return max(product_of_three_largest, product_of_two_smallest_and_largest)
