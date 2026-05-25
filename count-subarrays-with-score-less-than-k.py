class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        cur_sum = 0
        ans = 0
        while left < n:
            while right < n and (cur_sum + nums[right]) * (right - left + 1) < k:
                cur_sum += nums[right]
                right += 1
            ans += right - left
            if right == left:
                right += 1
            else:
                cur_sum -= nums[left]
            left += 1
        return ans