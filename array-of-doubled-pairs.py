class Solution:
    def canReorderDoubled(self, arr):
        from collections import Counter
        cnt = Counter(arr)
        for x in sorted(cnt, key=abs):
            if cnt[x] == 0:
                continue
            if cnt[2 * x] < cnt[x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True
