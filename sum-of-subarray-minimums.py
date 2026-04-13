from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        left = [0] * n
        stack = []
        for i in range(n):
            cnt = 1
            while stack and stack[-1][0] > arr[i]:
                _, c = stack.pop()
                cnt += c
            left[i] = cnt
            stack.append((arr[i], cnt))
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            cnt = 1
            while stack and stack[-1][0] >= arr[i]:
                _, c = stack.pop()
                cnt += c
            right[i] = cnt
            stack.append((arr[i], cnt))
        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % mod
        return ans
