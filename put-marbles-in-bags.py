class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k <= 1 or k >= n:
            return 0
        pair_sums = [weights[i] + weights[i+1] for i in range(n-1)]
        pair_sums.sort()
        m = k - 1
        min_sum = sum(pair_sums[:m])
        max_sum = sum(pair_sums[-m:])
        return max_sum - min_sum
