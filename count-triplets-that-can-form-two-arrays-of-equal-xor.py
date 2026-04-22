class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ arr[i]
        ans = 0
        for i in range(n):
            for k in range(i + 1, n):
                if pref[i] == pref[k + 1]:
                    ans += k - i
        return ans
