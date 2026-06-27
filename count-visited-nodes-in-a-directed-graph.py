from typing import List

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        state = [0] * n
        for i in range(n):
            if state[i]:
                continue
            stack = []
            pos = {}
            cur = i
            while state[cur] == 0:
                state[cur] = 1
                pos[cur] = len(stack)
                stack.append(cur)
                cur = edges[cur]
            if state[cur] == 1:
                cycle_start = pos[cur]
                cycle_len = len(stack) - cycle_start
                for j in range(cycle_start, len(stack)):
                    ans[stack[j]] = cycle_len
            for j in range(len(stack) - 1, -1, -1):
                node = stack[j]
                if ans[node] == 0:
                    ans[node] = ans[edges[node]] + 1
            for node in stack:
                state[node] = 2
        return ans
