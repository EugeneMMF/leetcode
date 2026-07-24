class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        diff = [0] * (n + 1)
        starts = [[] for _ in range(n)]
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
            starts[l].append(r)
        coverage = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            coverage[i] = cur
            if coverage[i] < nums[i]:
                return -1
        import heapq
        heap = []
        end_count = [0] * n
        active = 0
        selected = 0
        for i in range(n):
            for r in starts[i]:
                heapq.heappush(heap, -r)
            while active < nums[i]:
                if not heap:
                    return -1
                r = -heapq.heappop(heap)
                active += 1
                end_count[r] += 1
                selected += 1
            active -= end_count[i]
        return m - selected