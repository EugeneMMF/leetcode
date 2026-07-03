class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        import heapq
        counts = {}
        max_heap = []
        ans = []
        for val, d in zip(nums, freq):
            old = counts.get(val, 0)
            new = old + d
            if new == 0:
                counts.pop(val, None)
            else:
                counts[val] = new
            heapq.heappush(max_heap, (-new, val))
            while max_heap:
                c, v = max_heap[0]
                c = -c
                cur = counts.get(v, 0)
                if cur == c:
                    break
                heapq.heappop(max_heap)
            if max_heap:
                ans.append(-max_heap[0][0])
            else:
                ans.append(0)
        return ans