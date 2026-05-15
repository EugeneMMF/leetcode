class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                for c in range(b + 1, n - 1):
                    s = nums[a] + nums[b] + nums[c]
                    for d in range(c + 1, n):
                        if nums[d] == s:
                            count += 1
        return count
