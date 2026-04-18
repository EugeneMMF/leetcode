from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for s in arr:
            m = 0
            dup = False
            for ch in s:
                bit = 1 << (ord(ch) - 97)
                if m & bit:
                    dup = True
                    break
                m |= bit
            if not dup:
                masks.append((m, len(s)))
        best = 0
        def dfs(idx, cur_mask, cur_len):
            nonlocal best
            if cur_len > best:
                best = cur_len
            for i in range(idx, len(masks)):
                m, l = masks[i]
                if cur_mask & m == 0:
                    dfs(i + 1, cur_mask | m, cur_len + l)
        dfs(0, 0, 0)
        return best
