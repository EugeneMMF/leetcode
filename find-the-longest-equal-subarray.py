class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        ans = 0
        for indices in pos.values():
            l = 0
            for r in range(len(indices)):
                while l <= r:
                    L = indices[r] - indices[l] + 1
                    non_v = L - (r - l + 1)
                    if non_v <= k:
                        break
                    l += 1
                if l <= r:
                    ans = max(ans, r - l + 1)
        return ans
