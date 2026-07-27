class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = {}
        for i in range(n - k + 1):
            seen = set(nums[i:i+k])
            for v in seen:
                counts[v] = counts.get(v, 0) + 1
        ans = -1
        for v, c in counts.items():
            if c == 1 and v > ans:
                ans = v
        return ans
