from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen=set()
        left=0
        cur=0
        best=0
        for right,val in enumerate(nums):
            while val in seen:
                seen.remove(nums[left])
                cur-=nums[left]
                left+=1
            seen.add(val)
            cur+=val
            if cur>best:
                best=cur
        return best
