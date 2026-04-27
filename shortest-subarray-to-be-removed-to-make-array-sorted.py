class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        ans = min(n - left - 1, right)
        import bisect
        suffix = arr[right:]
        for i in range(left + 1):
            j = bisect.bisect_left(suffix, arr[i])
            if j < len(suffix):
                ans = min(ans, right + j - i - 1)
        return ans
