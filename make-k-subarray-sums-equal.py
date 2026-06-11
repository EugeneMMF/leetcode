class Solution:
    def makeSubKSumEqual(self, arr, k):
        from math import gcd
        n = len(arr)
        g = gcd(n, k)
        total = 0
        for offset in range(g):
            group = [arr[i] for i in range(offset, n, g)]
            group.sort()
            m = group[len(group) // 2]
            total += sum(abs(x - m) for x in group)
        return total