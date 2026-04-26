class Solution:
    def containsPattern(self, arr, m, k):
        n = len(arr)
        for i in range(n - m + 1):
            count = 1
            while i + count * m + m <= n and arr[i + (count - 1) * m:i + count * m] == arr[i + count * m:i + (count + 1) * m]:
                count += 1
                if count >= k:
                    return True
        return False
