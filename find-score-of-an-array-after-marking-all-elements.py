class Solution:
    def findScore(self, nums: List[int]) -> int:
        import heapq
        n = len(nums)
        marked = [False] * n
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        score = 0
        remaining = n
        while remaining:
            val, i = heapq.heappop(heap)
            if marked[i]:
                continue
            score += val
            marked[i] = True
            remaining -= 1
            if i - 1 >= 0 and not marked[i - 1]:
                marked[i - 1] = True
                remaining -= 1
            if i + 1 < n and not marked[i + 1]:
                marked[i + 1] = True
                remaining -= 1
        return score
