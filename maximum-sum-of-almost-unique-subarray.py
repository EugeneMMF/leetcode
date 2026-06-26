class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        from collections import defaultdict
        n = len(nums)
        if k > n:
            return 0
        freq = defaultdict(int)
        cur_sum = 0
        distinct = 0
        max_sum = 0
        for i in range(k):
            cur_sum += nums[i]
            if freq[nums[i]] == 0:
                distinct += 1
            freq[nums[i]] += 1
        if distinct >= m:
            max_sum = cur_sum
        for i in range(k, n):
            out_val = nums[i - k]
            cur_sum -= out_val
            freq[out_val] -= 1
            if freq[out_val] == 0:
                distinct -= 1
            in_val = nums[i]
            cur_sum += in_val
            if freq[in_val] == 0:
                distinct += 1
            freq[in_val] += 1
            if distinct >= m and cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
