class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_k(k):
            m = n // k
            return k * m * (m + 1) // 2
        return sum_k(3) + sum_k(5) + sum_k(7) - sum_k(15) - sum_k(21) - sum_k(35) + sum_k(105)
