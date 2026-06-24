from typing import List

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 4:
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                step = i
                start = i * i
                is_prime[start:n + 1:step] = [False] * (((n - start) // step) + 1)
        res = []
        for x in range(2, n // 2 + 1):
            if is_prime[x]:
                y = n - x
                if y >= x and is_prime[y]:
                    res.append([x, y])
        return res
