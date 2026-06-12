class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        from collections import Counter
        cnt = Counter(nums)
        max_freq = max(cnt.values())
        rows = [[] for _ in range(max_freq)]
        for num, c in cnt.items():
            for i in range(c):
                rows[i].append(num)
        return rows
