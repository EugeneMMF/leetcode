class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        freq = {}
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(x ** 0.5) + 1
            i = 3
            while i <= r:
                if x % i == 0:
                    return False
                i += 2
            return True
        for i in range(m):
            for j in range(n):
                for dr, dc in directions:
                    r, c = i, j
                    num = 0
                    while 0 <= r < m and 0 <= c < n:
                        num = num * 10 + mat[r][c]
                        if num > 10 and is_prime(num):
                            freq[num] = freq.get(num, 0) + 1
                        r += dr
                        c += dc
        if not freq:
            return -1
        max_freq = max(freq.values())
        candidates = [p for p, f in freq.items() if f == max_freq]
        return max(candidates) if candidates else -1