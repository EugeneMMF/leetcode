class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ones_taken = numOnes if numOnes < k else k
        remaining = k - ones_taken
        zeros_taken = numZeros if numZeros < remaining else remaining
        remaining -= zeros_taken
        return ones_taken - remaining