class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)
        ans = n
        for lst in pos.values():
            max_gap = 0
            for i in range(len(lst) - 1):
                diff = lst[i + 1] - lst[i]
                max_gap = max(max_gap, diff // 2)
            diff = lst[0] + n - lst[-1]
            max_gap = max(max_gap, diff // 2)
            ans = min(ans, max_gap)
        return ans
