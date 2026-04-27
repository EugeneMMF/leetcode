class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = n // 20
        arr.sort()
        trimmed = arr[k:n - k]
        return sum(trimmed) / len(trimmed)
