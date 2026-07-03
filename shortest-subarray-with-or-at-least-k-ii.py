class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        n = len(nums)
        bit_counts = [0] * 31
        left = 0
        ans = n + 1
        def cur_or():
            val = 0
            for b in range(31):
                if bit_counts[b]:
                    val |= (1 << b)
            return val
        for right in range(n):
            x = nums[right]
            for b in range(31):
                if x >> b & 1:
                    bit_counts[b] += 1
            while left <= right and cur_or() >= k:
                ans = min(ans, right - left + 1)
                y = nums[left]
                for b in range(31):
                    if y >> b & 1:
                        bit_counts[b] -= 1
                left += 1
        return ans if ans <= n else -1
