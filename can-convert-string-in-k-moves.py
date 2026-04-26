class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        if k == 0:
            return s == t
        required = [0] * 26
        for a, b in zip(s, t):
            if a != b:
                d = (ord(b) - ord(a)) % 26
                required[d] += 1
        for d in range(1, 26):
            if required[d]:
                if k < d:
                    return False
                available = (k - d) // 26 + 1
                if required[d] > available:
                    return False
        return True
