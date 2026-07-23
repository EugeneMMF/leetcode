class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if m > n:
            return 0
        req = [0] * 26
        for ch in word2:
            req[ord(ch) - 97] += 1
        cur = [0] * 26
        remaining = sum(req)
        l = 0
        r = -1
        ans = 0
        while l < n:
            while remaining > 0 and r + 1 < n:
                r += 1
                idx = ord(word1[r]) - 97
                if cur[idx] < req[idx]:
                    remaining -= 1
                cur[idx] += 1
            if remaining > 0:
                break
            ans += n - r
            idx_l = ord(word1[l]) - 97
            cur[idx_l] -= 1
            if cur[idx_l] < req[idx_l]:
                remaining += 1
            l += 1
        return ans