class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        result = 0
        center = False
        for w, cnt in list(counts.items()):
            rev = w[::-1]
            if w == rev:
                result += (cnt // 2) * 4
                if cnt % 2 == 1:
                    center = True
            elif w < rev:
                rev_cnt = counts.get(rev, 0)
                pairs = min(cnt, rev_cnt)
                result += pairs * 4
        if center:
            result += 2
        return result