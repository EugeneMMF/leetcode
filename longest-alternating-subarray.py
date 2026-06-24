class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = -1
        cur_len = 0
        prev_diff = 0
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                if prev_diff == -1:
                    cur_len += 1
                else:
                    cur_len = 2
                prev_diff = 1
                if cur_len > max_len:
                    max_len = cur_len
            elif diff == -1:
                if prev_diff == 1:
                    cur_len += 1
                    prev_diff = -1
                    if cur_len > max_len:
                        max_len = cur_len
                else:
                    cur_len = 0
                    prev_diff = 0
            else:
                cur_len = 0
                prev_diff = 0
        return max_len if max_len >= 2 else -1