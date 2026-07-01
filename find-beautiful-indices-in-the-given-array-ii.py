class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp_occurrences(text, pattern):
            n, m = len(text), len(pattern)
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
        import bisect
        a_pos = kmp_occurrences(s, a)
        b_pos = kmp_occurrences(s, b)
        res = []
        for i in a_pos:
            left = bisect.bisect_left(b_pos, i - k)
            if left < len(b_pos) and abs(b_pos[left] - i) <= k:
                res.append(i)
            elif left > 0 and abs(b_pos[left - 1] - i) <= k:
                res.append(i)
        return res
