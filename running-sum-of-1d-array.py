class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        res = []
        for x in nums:
            total += x
            res.append(total)
        return res
