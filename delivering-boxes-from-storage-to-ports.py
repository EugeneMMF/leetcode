class Solution:
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        n = len(boxes)
        ports = [0] * (n + 1)
        weights = [0] * (n + 1)
        for i, (p, w) in enumerate(boxes, 1):
            ports[i] = p
            weights[i] = w
        preWeight = [0] * (n + 1)
        prePortChange = [0] * (n + 1)
        for i in range(1, n + 1):
            preWeight[i] = preWeight[i - 1] + weights[i]
            prePortChange[i] = prePortChange[i - 1] + (1 if i > 1 and ports[i] != ports[i - 1] else 0)
        dp = [0] * (n + 1)
        from collections import deque
        dq = deque()
        dq.append((0, dp[0] - prePortChange[1]))
        left = 1
        for i in range(1, n + 1):
            while i - left + 1 > maxBoxes or preWeight[i] - preWeight[left - 1] > maxWeight:
                left += 1
            while dq and dq[0][0] < left - 1:
                dq.popleft()
            dp[i] = dq[0][1] + prePortChange[i] + 2
            if i < n:
                val = dp[i] - prePortChange[i + 1]
                while dq and dq[-1][1] >= val:
                    dq.pop()
                dq.append((i, val))
        return dp[n]
