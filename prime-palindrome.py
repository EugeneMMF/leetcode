class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            for p in [11]:
                if p >= n:
                    return p
        for length in range(1, 10, 2):
            half = (length + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half
            for i in range(start, end):
                s = str(i)
                pal = int(s + s[-2::-1])
                if pal >= n and is_prime(pal):
                    return pal
        return 100030001
