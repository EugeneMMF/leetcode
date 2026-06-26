class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        break_count = 0
        break_index = -1
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                break_count += 1
                break_index = i
        if break_count == 0:
            return 0
        if break_count > 1:
            return -1
        min_index = (break_index + 1) % n
        return (n - min_index) % n