class Solution:
    def prevPermOpt1(self, arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr
        max_val = -1
        for k in range(i + 1, n):
            if arr[k] < arr[i] and arr[k] > max_val:
                max_val = arr[k]
        j = -1
        for k in range(i + 1, n):
            if arr[k] == max_val:
                j = k
                break
        arr[i], arr[j] = arr[j], arr[i]
        return arr
