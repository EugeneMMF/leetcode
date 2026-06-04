class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq
        n = len(costs)
        left_end = candidates - 1
        right_start = n - candidates
        left_heap = []
        right_heap = []
        for i in range(candidates):
            heapq.heappush(left_heap, (costs[i], i))
        for i in range(n - 1, n - candidates - 1, -1):
            if i > left_end:
                heapq.heappush(right_heap, (costs[i], i))
        left_ptr = candidates
        right_ptr = n - candidates - 1
        total = 0
        for _ in range(k):
            if left_heap and right_heap:
                if left_heap[0] <= right_heap[0]:
                    cost, idx = heapq.heappop(left_heap)
                    total += cost
                    if left_ptr <= right_ptr:
                        heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                        left_ptr += 1
                else:
                    cost, idx = heapq.heappop(right_heap)
                    total += cost
                    if right_ptr >= left_ptr:
                        heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                        right_ptr -= 1
            elif left_heap:
                cost, idx = heapq.heappop(left_heap)
                total += cost
                if left_ptr <= right_ptr:
                    heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                    left_ptr += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if right_ptr >= left_ptr:
                    heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                    right_ptr -= 1
        return total