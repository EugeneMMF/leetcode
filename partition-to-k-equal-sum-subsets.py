class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % k != 0:
            return False

        target_sum = total_sum // k

        nums.sort(reverse=True)

        if nums[0] > target_sum:
            return False

        memo = {}

        def solve(bucket_idx, current_sum, used_mask):
            if bucket_idx == k:
                return True

            if current_sum == target_sum:
                return solve(bucket_idx + 1, 0, used_mask)

            if (used_mask, current_sum) in memo:
                return memo[(used_mask, current_sum)]

            for i in range(n):
                if (used_mask >> i) & 1:
                    continue

                if current_sum + nums[i] > target_sum:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not ((used_mask >> (i-1)) & 1):
                    continue

                if solve(bucket_idx, current_sum + nums[i], used_mask | (1 << i)):
                    memo[(used_mask, current_sum)] = True
                    return True

            memo[(used_mask, current_sum)] = False
            return False

        return solve(0, 0, 0)
