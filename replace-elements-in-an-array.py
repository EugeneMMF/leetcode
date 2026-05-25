from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {value: i for i, value in enumerate(nums)}
        for old, new in operations:
            i = index_map[old]
            nums[i] = new
            del index_map[old]
            index_map[new] = i
        return nums
