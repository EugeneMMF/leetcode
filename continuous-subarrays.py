class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        from collections import deque
        maxD = deque()
        minD = deque()
        left = 0
        res = 0
        for right, val in enumerate(nums):
            while maxD and nums[maxD[-1]] <= val:
                maxD.pop()
            maxD.append(right)
            while minD and nums[minD[-1]] >= val:
                minD.pop()
            minD.append(right)
            while nums[maxD[0]] - nums[minD[0]] > 2:
                left += 1
                if maxD[0] < left:
                    maxD.popleft()
                if minD[0] < left:
                    minD.popleft()
            res += right - left + 1
        return res
