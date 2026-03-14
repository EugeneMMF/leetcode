class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def check(max_sum_candidate: int) -> bool:
            num_subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num <= max_sum_candidate:
                    current_sum += num
                else:
                    num_subarrays += 1
                    current_sum = num
                    if num_subarrays > k:
                        return False
            return True

        left = max(nums)
        right = sum(nums)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
