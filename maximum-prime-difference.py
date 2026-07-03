class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
        first = None
        last = None
        for i, v in enumerate(nums):
            if v in primes:
                if first is None:
                    first = i
                last = i
        return 0 if first is None else last - first