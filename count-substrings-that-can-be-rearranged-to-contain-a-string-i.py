class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if m > n:
            return 0
        req = [0] * 26
        for ch in word2:
            req[ord(ch) - 97] += 1
        need = sum(1 for x in req if x > 0)
        cnt = [0] * 26
        res = 0
        end = 0
        for start in range(n):
            while end < n and need > 0:
                idx = ord(word1[end]) - 97
                cnt[idx] += 1
                if cnt[idx] == req[idx]:
                    need -= 1
                end += 1
            if need == 0:
                res += n - end + 1
            idx_start = ord(word1[start]) - 97
            if cnt[idx_start] == req[idx_start]:
                need += 1
            cnt[idx_start] -= 1
        return res