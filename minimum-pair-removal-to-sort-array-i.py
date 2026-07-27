class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while len(nums) > 1:
            sorted_flag = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    sorted_flag = False
                    break
            if sorted_flag:
                break
            min_sum = nums[0] + nums[1]
            idx = 0
            for i in range(1, len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            nums[idx] = min_sum
            del nums[idx + 1]
            ops += 1
        return ops
