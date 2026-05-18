class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def to_base(num, base):
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits)) if digits else '0'
        count = 0
        total = 0
        length = 1
        while count < n:
            if length == 1:
                for d in range(1, 10):
                    if count >= n:
                        break
                    num = d
                    b = to_base(num, k)
                    if b == b[::-1]:
                        total += num
                        count += 1
                length += 1
                continue
            half = (length + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half
            for i in range(start, end):
                if count >= n:
                    break
                s = str(i)
                if length % 2 == 0:
                    pal = int(s + s[::-1])
                else:
                    pal = int(s + s[-2::-1])
                b = to_base(pal, k)
                if b == b[::-1]:
                    total += pal
                    count += 1
            length += 1
        return total