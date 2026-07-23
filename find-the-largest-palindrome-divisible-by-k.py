class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if n <= 0:
            return ""
        m = (n + 1) // 2
        pow10 = [0] * n
        if n > 0:
            pow10[0] = 1 % k
            for i in range(1, n):
                pow10[i] = (pow10[i - 1] * 10) % k
        coeff = [0] * m
        for p in range(m):
            j = n - 1 - p
            if p == j:
                coeff[p] = pow10[p] % k
            else:
                coeff[p] = (pow10[j] + pow10[p]) % k
        can = [bytearray(k) for _ in range(m + 1)]
        can[m][0] = 1
        for pos in range(m - 1, -1, -1):
            arr_next = can[pos + 1]
            arr = can[pos]
            if pos == 0:
                digits = range(1, 10)
            else:
                digits = range(0, 10)
            c = coeff[pos]
            for d in digits:
                cd = (c * d) % k
                for s in range(k):
                    if arr_next[s]:
                        r = (cd + s) % k
                        arr[r] = 1
        res_digits = []
        rem = 0
        for pos in range(0, m):
            if pos == 0:
                digits = range(9, 0, -1)
            else:
                digits = range(9, -1, -1)
            found = False
            c = coeff[pos]
            for d in digits:
                cd = (c * d) % k
                new_rem = (rem + cd) % k
                target = (-new_rem) % k
                if can[pos + 1][target]:
                    res_digits.append(str(d))
                    rem = new_rem
                    found = True
                    break
            if not found:
                return ""
        if n % 2 == 0:
            left = "".join(res_digits)
            right = left[::-1]
            return left + right
        else:
            left = "".join(res_digits[:-1])
            mid = res_digits[-1]
            return left + mid + left[::-1]
