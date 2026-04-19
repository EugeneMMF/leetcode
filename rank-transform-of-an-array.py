class Solution:
    def arrayRankTransform(self, arr):
        if not arr:
            return []
        sorted_unique = sorted(set(arr))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        return [rank[x] for x in arr]
