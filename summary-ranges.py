from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        n = len(nums)
        i = 0

        while i < n:
            start = nums[i]
            j = i

            while j + 1 < n and nums[j+1] == nums[j] + 1:
                j += 1
            
            end = nums[j]

            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            
            i = j + 1
        
        return result
