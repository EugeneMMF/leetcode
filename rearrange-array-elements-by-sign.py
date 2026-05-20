from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for x in nums:
            if x > 0:
                positives.append(x)
            else:
                negatives.append(x)
        result = []
        for p, n in zip(positives, negatives):
            result.append(p)
            result.append(n)
        return result
