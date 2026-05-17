class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        from collections import deque
        max_val = 1000
        visited = [False] * (max_val + 1)
        queue = deque()
        queue.append((start, 0))
        visited[start] = True
        while queue:
            cur, steps = queue.popleft()
            for v in nums:
                for nxt in (cur + v, cur - v, cur ^ v):
                    if nxt == goal:
                        return steps + 1
                    if 0 <= nxt <= max_val and not visited[nxt]:
                        visited[nxt] = True
                        queue.append((nxt, steps + 1))
        return -1