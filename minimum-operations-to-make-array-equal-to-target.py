class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        prev = 0
        ans = 0
        for d in (t - n for n, t in zip(nums, target)):
            if d > prev:
                ans += d - prev
            prev = d
        if prev < 0:
            ans += -prev
        return ans
