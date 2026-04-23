class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) < k:
            return False
        seen = set()
        cur = 0
        mask = need - 1
        for i, ch in enumerate(s):
            cur = ((cur << 1) & mask) | (ch == '1')
            if i >= k - 1:
                seen.add(cur)
                if len(seen) == need:
                    return True
        return len(seen) == need
