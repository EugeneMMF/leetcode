class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        block = [0] * n
        cur = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cur += 1
            block[i] = cur
        return [block[u] == block[v] for u, v in queries]
