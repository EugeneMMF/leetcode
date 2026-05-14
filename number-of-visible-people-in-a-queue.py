import typing

class Solution:
    def canSeePersonsCount(self, heights: typing.List[int]) -> typing.List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            cnt = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                cnt += 1
            if stack:
                cnt += 1
            ans[i] = cnt
            stack.append(heights[i])
        return ans
