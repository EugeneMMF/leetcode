class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        k = num2.bit_count()
        x = 0
        need = k
        for i in range(31, -1, -1):
            if (num1 >> i) & 1:
                if need:
                    x |= 1 << i
                    need -= 1
        if need:
            for i in range(32):
                if ((num1 >> i) & 1) == 0:
                    x |= 1 << i
                    need -= 1
                    if not need:
                        break
        return x
