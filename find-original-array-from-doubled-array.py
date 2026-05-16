class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        from collections import Counter
        if len(changed) % 2 != 0:
            return []
        cnt = Counter(changed)
        res = []
        for x in sorted(cnt):
            if cnt[x] == 0:
                continue
            if x == 0:
                if cnt[x] % 2 != 0:
                    return []
                res.extend([0] * (cnt[x] // 2))
                cnt[x] = 0
                continue
            y = x * 2
            if cnt[y] < cnt[x]:
                return []
            res.extend([x] * cnt[x])
            cnt[y] -= cnt[x]
            cnt[x] = 0
        return res
