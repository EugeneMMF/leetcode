class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        import math
        L = int(left)
        R = int(right)
        max_root = int(math.isqrt(R)) + 1
        def is_pal(x):
            s = str(x)
            return s == s[::-1]
        count = 0
        i = 1
        while True:
            s = str(i)
            even = int(s + s[::-1])
            if even > max_root:
                break
            sq = even * even
            if sq >= L and sq <= R and is_pal(sq):
                count += 1
            i += 1
        i = 1
        while True:
            s = str(i)
            odd = int(s + s[-2::-1])
            if odd > max_root:
                break
            sq = odd * odd
            if sq >= L and sq <= R and is_pal(sq):
                count += 1
            i += 1
        return count
