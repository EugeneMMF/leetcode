from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        res = [0] * n
        if k > 0:
            for i in range(n):
                s = 0
                for j in range(1, k + 1):
                    s += code[(i + j) % n]
                res[i] = s
        else:
            m = -k
            for i in range(n):
                s = 0
                for j in range(1, m + 1):
                    s += code[(i - j) % n]
                res[i] = s
        return res
