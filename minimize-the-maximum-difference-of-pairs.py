class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        def can(d):
            i = 0
            cnt = 0
            n = len(nums)
            while i + 1 < n:
                if nums[i+1] - nums[i] <= d:
                    cnt += 1
                    i += 2
                    if cnt >= p:
                        return True
                else:
                    i += 1
            return cnt >= p
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        return low