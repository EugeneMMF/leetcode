class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        large = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
                if n // i != i:
                    large.append(n // i)
            i += 1
        if k > 0 and k <= len(large):
            return large[-k]
        return -1
