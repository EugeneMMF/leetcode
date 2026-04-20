class Solution:
    def isPossible(self, target):
        import heapq
        if len(target) == 1:
            return target[0] == 1
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        while True:
            mx = -heapq.heappop(heap)
            rest = total - mx
            if mx == 1 or rest == 1:
                return True
            if rest == 0 or mx < rest or mx % rest == 0:
                return False
            new_val = mx % rest
            total = rest + new_val
            heapq.heappush(heap, -new_val)
