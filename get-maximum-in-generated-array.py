class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        max_val = 1
        i = 1
        while 2 * i <= n:
            nums[2 * i] = nums[i]
            if nums[2 * i] > max_val:
                max_val = nums[2 * i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
                if nums[2 * i + 1] > max_val:
                    max_val = nums[2 * i + 1]
            i += 1
        return max_val
