class Solution:
    def waysToMakeFair(self, nums):
        n = len(nums)
        prefix_even = [0] * (n + 1)
        prefix_odd = [0] * (n + 1)
        for i in range(n):
            prefix_even[i + 1] = prefix_even[i] + (nums[i] if i % 2 == 0 else 0)
            prefix_odd[i + 1] = prefix_odd[i] + (nums[i] if i % 2 == 1 else 0)
        total_even = prefix_even[n]
        total_odd = prefix_odd[n]
        ans = 0
        for i in range(n):
            even_after = prefix_even[i] + (total_odd - prefix_odd[i + 1])
            odd_after = prefix_odd[i] + (total_even - prefix_even[i + 1])
            if even_after == odd_after:
                ans += 1
        return ans
