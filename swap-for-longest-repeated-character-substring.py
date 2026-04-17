class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        if n == 0:
            return 0
        from collections import Counter, defaultdict
        total = Counter(text)
        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j
        ans = 0
        m = len(groups)
        for idx, (ch, length) in enumerate(groups):
            if total[ch] > length:
                ans = max(ans, length + 1)
            else:
                ans = max(ans, length)
            if idx + 2 < m and groups[idx + 1][1] == 1 and groups[idx + 2][0] == ch:
                merged = length + groups[idx + 2][1]
                if total[ch] > merged:
                    merged += 1
                ans = max(ans, merged)
        return ans
