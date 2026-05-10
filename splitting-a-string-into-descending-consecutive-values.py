class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        for mask in range(1, 1 << (n - 1)):
            prev = None
            start = 0
            ok = True
            for i in range(n - 1):
                if mask >> i & 1:
                    cur = int(s[start:i + 1])
                    if prev is None:
                        prev = cur
                    else:
                        if cur != prev - 1:
                            ok = False
                            break
                        prev = cur
                    start = i + 1
            if not ok:
                continue
            cur = int(s[start:n])
            if prev is None:
                continue
            if cur != prev - 1:
                continue
            return True
        return False
