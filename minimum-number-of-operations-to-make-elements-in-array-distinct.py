class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        max_ops = (n + 2) // 3
        for k in range(max_ops + 1):
            start = 3 * k
            if start >= n:
                return k
            sub = nums[start:]
            if len(sub) == len(set(sub)):
                return k
        return max_ops
