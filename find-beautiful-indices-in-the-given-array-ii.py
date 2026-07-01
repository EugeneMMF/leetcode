class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp_positions(text, pattern):
            n, m = len(text), len(pattern)
            if m == 0 or n < m:
                return []
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            res = []
            i = j = 0
            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                if j == m:
                    res.append(i - j)
                    j = lps[j - 1]
                elif i < n and text[i] != pattern[j]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return res
        pos_a = kmp_positions(s, a)
        pos_b = kmp_positions(s, b)
        import bisect
        res = []
        for i in pos_a:
            idx = bisect.bisect_left(pos_b, i - k)
            if idx < len(pos_b) and abs(pos_b[idx] - i) <= k:
                res.append(i)
        return res
