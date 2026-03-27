import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        
        for x in nums:
            # Add all initial numbers to the heap
            heapq.heappush(self.min_heap, x)
        
        # If the heap size exceeds k, remove the smallest elements until it's size k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # If the heap has less than k elements, simply add the new value
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If the heap is full (contains k elements) and the new value is greater
        # than the smallest element in the heap (which is the current kth largest)
        elif val > self.min_heap[0]:
            # Remove the smallest element and add the new value
            heapq.heapreplace(self.min_heap, val)
        
        # The smallest element in the min-heap is the kth largest element in the stream
        return self.min_heap[0]
