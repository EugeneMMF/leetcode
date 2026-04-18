from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_cnt = Counter(letters)
        n = len(words)
        word_counts = []
        word_scores = []
        for w in words:
            cnt = Counter(w)
            word_counts.append(cnt)
            word_scores.append(sum(cnt[ch] * score[ord(ch) - 97] for ch in cnt))
        best = 0
        def dfs(i, avail, cur):
            nonlocal best
            if i == n:
                if cur > best:
                    best = cur
                return
            dfs(i + 1, avail, cur)
            wc = word_counts[i]
            for ch, c in wc.items():
                if avail.get(ch, 0) < c:
                    break
            else:
                for ch, c in wc.items():
                    avail[ch] -= c
                dfs(i + 1, avail, cur + word_scores[i])
                for ch, c in wc.items():
                    avail[ch] += c
        dfs(0, letters_cnt, 0)
        return best
