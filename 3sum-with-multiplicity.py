class Solution:
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        freq = [0] * 101
        for v in arr:
            freq[v] += 1
        ans = 0
        for i in range(101):
            if freq[i] == 0:
                continue
            for j in range(i, 101):
                if freq[j] == 0:
                    continue
                k = target - i - j
                if k < j or k > 100:
                    continue
                if freq[k] == 0:
                    continue
                if i == j == k:
                    cnt = freq[i] * (freq[i] - 1) * (freq[i] - 2) // 6
                elif i == j != k:
                    cnt = freq[i] * (freq[i] - 1) // 2 * freq[k]
                elif i < j == k:
                    cnt = freq[j] * (freq[j] - 1) // 2 * freq[i]
                else:
                    cnt = freq[i] * freq[j] * freq[k]
                ans = (ans + cnt) % MOD
        return ans
