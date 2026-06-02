class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        from collections import deque
        n = len(chargeTimes)
        l = 0
        sumRun = 0
        maxDeque = deque()
        ans = 0
        for r in range(n):
            sumRun += runningCosts[r]
            while maxDeque and chargeTimes[maxDeque[-1]] <= chargeTimes[r]:
                maxDeque.pop()
            maxDeque.append(r)
            while l <= r and chargeTimes[maxDeque[0]] + (r - l + 1) * sumRun > budget:
                if maxDeque[0] == l:
                    maxDeque.popleft()
                sumRun -= runningCosts[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
