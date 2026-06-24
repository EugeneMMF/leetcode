import math
from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        if not words:
            return 0
        w0 = words[0]
        prev = {(w0[0], w0[-1]): len(w0)}
        for w in words[1:]:
            w_len = len(w)
            w_f, w_l = w[0], w[-1]
            cur = {}
            for (f, l), L in prev.items():
                # join(prev, w)
                new_f, new_l = f, w_l
                new_len = L + w_len - (1 if l == w_f else 0)
                key = (new_f, new_l)
                if key not in cur or new_len < cur[key]:
                    cur[key] = new_len
                # join(w, prev)
                new_f, new_l = w_f, l
                new_len = L + w_len - (1 if w_l == f else 0)
                key = (new_f, new_l)
                if key not in cur or new_len < cur[key]:
                    cur[key] = new_len
            prev = cur
        return min(prev.values())