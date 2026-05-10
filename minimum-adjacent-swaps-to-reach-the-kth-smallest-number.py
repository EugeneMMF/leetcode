class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        arr = list(num)
        def next_perm(a):
            i = len(a) - 2
            while i >= 0 and a[i] >= a[i + 1]:
                i -= 1
            if i == -1:
                return False
            j = len(a) - 1
            while a[j] <= a[i]:
                j -= 1
            a[i], a[j] = a[j], a[i]
            a[i + 1 :] = reversed(a[i + 1 :])
            return True
        for _ in range(k):
            next_perm(arr)
        target = arr
        curr = list(num)
        swaps = 0
        n = len(num)
        for i in range(n):
            if curr[i] == target[i]:
                continue
            j = i + 1
            while curr[j] != target[i]:
                j += 1
            while j > i:
                curr[j], curr[j - 1] = curr[j - 1], curr[j]
                j -= 1
                swaps += 1
        return swaps