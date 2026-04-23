class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = 10**9
        left = [INF] * n
        s = 0
        l = 0
        best = INF
        for r in range(n):
            s += arr[r]
            while s > target:
                s -= arr[l]
                l += 1
            if s == target:
                length = r - l + 1
                if length < best:
                    best = length
            left[r] = best
        right = [INF] * n
        s = 0
        r = n - 1
        best = INF
        for l in range(n - 1, -1, -1):
            s += arr[l]
            while s > target:
                s -= arr[r]
                r -= 1
            if s == target:
                length = r - l + 1
                if length < best:
                    best = length
            right[l] = best
        ans = INF
        for i in range(n - 1):
            if left[i] != INF and right[i + 1] != INF:
                total = left[i] + right[i + 1]
                if total < ans:
                    ans = total
        return -1 if ans == INF else ans
