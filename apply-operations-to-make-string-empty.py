class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        max_count = max(freq)
        last_idx = [-1] * 26
        for i, ch in enumerate(s):
            last_idx[ord(ch) - 97] = i
        res = []
        for i in range(26):
            if freq[i] == max_count:
                res.append((last_idx[i], chr(i + 97)))
        res.sort()
        return ''.join(ch for _, ch in res)
