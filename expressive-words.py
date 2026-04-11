from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def encode(t):
            chars = []
            counts = []
            i = 0
            n = len(t)
            while i < n:
                j = i
                while j < n and t[j] == t[i]:
                    j += 1
                chars.append(t[i])
                counts.append(j - i)
                i = j
            return chars, counts
        s_chars, s_counts = encode(s)
        ans = 0
        for w in words:
            w_chars, w_counts = encode(w)
            if w_chars != s_chars:
                continue
            ok = True
            for sc, wc in zip(s_counts, w_counts):
                if sc < 3:
                    if wc != sc:
                        ok = False
                        break
                else:
                    if wc > sc:
                        ok = False
                        break
            if ok:
                ans += 1
        return ans
