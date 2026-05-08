class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        pos = [c[0] for c in cars]
        sp = [c[1] for c in cars]
        ans = [-1.0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack:
                j = stack[-1]
                if sp[i] <= sp[j]:
                    stack.pop()
                    continue
                t = (pos[j] - pos[i]) / (sp[i] - sp[j])
                if ans[j] == -1 or t <= ans[j]:
                    ans[i] = t
                    break
                stack.pop()
            stack.append(i)
        return ans
