class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = [False] * 101
        for start, end in nums:
            for i in range(start, end + 1):
                covered[i] = True
        return sum(covered)