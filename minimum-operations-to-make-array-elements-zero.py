class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        powers = [1]
        while powers[-1] <= 10**9:
            powers.append(powers[-1] * 4)
        max_k = len(powers)
        total_ops = 0
        for l, r in queries:
            total_steps = 0
            for k in range(1, max_k):
                low = powers[k-1]
                high = powers[k] - 1
                start = l if l > low else low
                end = r if r < high else high
                if start <= end:
                    total_steps += (end - start + 1) * k
            total_ops += (total_steps + 1) // 2
        return total_ops
