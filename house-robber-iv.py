class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can(limit: int) -> bool:
            skip = 0
            take = -10**9
            for val in nums:
                if val <= limit:
                    new_take = skip + 1
                    new_skip = max(skip, take)
                else:
                    new_take = -10**9
                    new_skip = max(skip, take)
                skip, take = new_skip, new_take
            return max(skip, take) >= k
        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        return low