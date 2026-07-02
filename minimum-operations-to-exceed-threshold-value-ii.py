class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        ops = 0
        while len(nums) > 1 and nums[0] < k:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            heapq.heappush(nums, a * 2 + b)
            ops += 1
        return ops
