class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        best = [0, 0, 0]
        for x in nums:
            if x == 1:
                best[0] += 1
            elif x == 2:
                best[1] = max(best[0], best[1]) + 1
            else:
                best[2] = max(best[0], best[1], best[2]) + 1
        return len(nums) - max(best)
