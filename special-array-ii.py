class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        bad = [0] * n
        for i in range(1, n):
            bad[i] = bad[i - 1] + (nums[i] % 2 == nums[i - 1] % 2)
        res = []
        for l, r in queries:
            if l == r:
                res.append(True)
            else:
                res.append(bad[r] - bad[l] == 0)
        return res