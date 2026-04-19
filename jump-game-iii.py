from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        stack = [start]
        while stack:
            i = stack.pop()
            if visited[i]:
                continue
            visited[i] = True
            if arr[i] == 0:
                return True
            jump = arr[i]
            nxt = i + jump
            if 0 <= nxt < n and not visited[nxt]:
                stack.append(nxt)
            nxt = i - jump
            if 0 <= nxt < n and not visited[nxt]:
                stack.append(nxt)
        return False
