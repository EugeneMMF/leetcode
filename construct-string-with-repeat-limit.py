class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        res = []
        while True:
            i = 25
            while i >= 0 and cnt[i] == 0:
                i -= 1
            if i < 0:
                break
            use = min(cnt[i], repeatLimit)
            res.append(chr(i + 97) * use)
            cnt[i] -= use
            if cnt[i] == 0:
                continue
            j = i - 1
            while j >= 0 and cnt[j] == 0:
                j -= 1
            if j < 0:
                break
            res.append(chr(j + 97))
            cnt[j] -= 1
        return ''.join(res)
