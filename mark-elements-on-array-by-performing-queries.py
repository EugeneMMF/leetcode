class Solution:
    def unmarkedSumArray(self, nums, queries):
        import heapq
        n = len(nums)
        marked = [False] * n
        total = sum(nums)
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        ans = []
        for idx, k in queries:
            if not marked[idx]:
                marked[idx] = True
                total -= nums[idx]
            cnt = 0
            while cnt < k and heap:
                v, i = heapq.heappop(heap)
                if marked[i]:
                    continue
                marked[i] = True
                total -= v
                cnt += 1
            ans.append(total)
        return ans
