class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        pref = [[0] * (n + 1) for _ in range(101)]
        for i, val in enumerate(nums, 1):
            for v in range(1, 101):
                pref[v][i] = pref[v][i - 1]
            pref[val][i] += 1
        ans = []
        for l, r in queries:
            present = []
            for v in range(1, 101):
                if pref[v][r + 1] - pref[v][l] > 0:
                    present.append(v)
            if len(present) < 2:
                ans.append(-1)
            else:
                min_diff = 101
                for i in range(1, len(present)):
                    diff = present[i] - present[i - 1]
                    if diff < min_diff:
                        min_diff = diff
                ans.append(min_diff)
        return ans
