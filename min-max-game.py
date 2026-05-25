class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new = []
            for i in range(0, len(nums), 2):
                if (i // 2) % 2 == 0:
                    new.append(min(nums[i], nums[i + 1]))
                else:
                    new.append(max(nums[i], nums[i + 1]))
            nums = new
        return nums[0]
