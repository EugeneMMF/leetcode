class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:
            diff_left = abs(arr[left] - x)
            diff_right = abs(arr[right] - x)

            if diff_left <= diff_right:
                # If arr[left] is closer or equally close to x,
                # and arr[left] < arr[right] (due to sorted array and left < right),
                # then arr[left] is preferred.
                # So, we discard arr[right] by moving the right pointer inwards.
                right -= 1
            else:
                # arr[right] is strictly closer to x,
                # so we discard arr[left] by moving the left pointer inwards.
                left += 1
        
        return arr[left : right + 1]
