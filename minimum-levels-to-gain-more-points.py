class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        total_ones = sum(possible)
        ones_prefix = 0
        for k in range(1, n):
            ones_prefix += possible[k - 1]
            alice = 2 * ones_prefix - k
            bob = 2 * (total_ones - ones_prefix) - (n - k)
            if alice > bob:
                return k
        return -1