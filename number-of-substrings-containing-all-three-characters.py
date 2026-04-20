class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = {'a':0,'b':0,'c':0}
        left = 0
        right = 0
        res = 0
        while left < n:
            while right < n and (cnt['a']==0 or cnt['b']==0 or cnt['c']==0):
                cnt[s[right]] += 1
                right += 1
            if cnt['a'] and cnt['b'] and cnt['c']:
                res += n - right + 1
            cnt[s[left]] -= 1
            left += 1
        return res
