from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts={}
        for i in range(len(nums)-1):
            if nums[i]==key:
                nxt=nums[i+1]
                counts[nxt]=counts.get(nxt,0)+1
        return max(counts, key=counts.get)
