class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        from bisect import bisect_right
        n = len(nums)
        next_greater = [n] * n
        stack = []
        for i, v in enumerate(nums):
            while stack and v > nums[stack[-1]]:
                idx = stack.pop()
                next_greater[idx] = i
            stack.append(i)
        val_to_indices = {}
        pos_in_list = [0] * n
        for i, v in enumerate(nums):
            if v not in val_to_indices:
                val_to_indices[v] = []
            pos_in_list[i] = len(val_to_indices[v])
            val_to_indices[v].append(i)
        ans = 0
        for i, v in enumerate(nums):
            R = next_greater[i]
            idx_list = val_to_indices[v]
            pos = pos_in_list[i]
            endpos = bisect_right(idx_list, R - 1)
            ans += (endpos - (pos + 1)) + 1
        return ans
