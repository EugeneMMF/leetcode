class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def calculate_sum(divisor: int) -> int:
            current_sum = 0
            for num in nums:
                current_sum += (num + divisor - 1) // divisor
            return current_sum

        left = 1
        right = max(nums)
        
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            
            if calculate_sum(mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
