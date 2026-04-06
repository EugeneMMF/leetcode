class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        max_right = -1
        for i in range(n - 1, -1, -1):
            current_element = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current_element)
        return arr
