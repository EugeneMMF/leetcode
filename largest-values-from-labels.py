class Solution:
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        items = sorted(zip(values, labels), reverse=True)
        cnt = {}
        total = 0
        taken = 0
        for v, l in items:
            if taken == numWanted:
                break
            if cnt.get(l, 0) < useLimit:
                total += v
                cnt[l] = cnt.get(l, 0) + 1
                taken += 1
        return total
