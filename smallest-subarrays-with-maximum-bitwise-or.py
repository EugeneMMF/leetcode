from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        B = 31
        next_pos = [[n]*B for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            curr = nums[i]
            for b in range(B):
                if curr >> b & 1:
                    next_pos[i][b] = i
                else:
                    next_pos[i][b] = next_pos[i+1][b]
        suff_or = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suff_or[i] = nums[i] | suff_or[i+1]
        ans = [0]*n
        for i in range(n):
            max_index = i
            val = suff_or[i]
            for b in range(B):
                if val >> b & 1:
                    idx = next_pos[i][b]
                    if idx > max_index:
                        max_index = idx
            ans[i] = max_index - i + 1
        return ans
