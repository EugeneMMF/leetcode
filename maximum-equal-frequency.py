class Solution:
    def maxEqualFreq(self, nums):
        from collections import defaultdict
        cnt = defaultdict(int)
        freq = defaultdict(int)
        ans = 0
        maxFreq = 0
        for i, x in enumerate(nums):
            prev = cnt[x]
            if prev:
                freq[prev] -= 1
                if freq[prev] == 0:
                    del freq[prev]
            cnt[x] = prev + 1
            cur = cnt[x]
            freq[cur] += 1
            maxFreq = max(maxFreq, cur)
            total = i + 1
            cond = False
            if maxFreq == 1:
                cond = True
            elif freq[maxFreq] == 1 and (maxFreq - 1) * (freq.get(maxFreq - 1, 0)) + maxFreq == total:
                cond = True
            elif freq.get(1, 0) == 1 and maxFreq * freq[maxFreq] + 1 == total:
                cond = True
            if cond:
                ans = total
        return ans
