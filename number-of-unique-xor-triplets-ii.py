class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pair_xors = set()
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                pair_xors.add(nums[i] ^ nums[j])
        triplet_xors = set()
        for p in pair_xors:
            for v in nums:
                triplet_xors.add(p ^ v)
        return len(triplet_xors)
