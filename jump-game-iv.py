from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        from collections import deque, defaultdict
        idx_map = defaultdict(list)
        for i, v in enumerate(arr):
            idx_map[v].append(i)
        dq = deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0
        while dq:
            for _ in range(len(dq)):
                i = dq.popleft()
                if i == n - 1:
                    return steps
                nxt = i + 1
                if nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
                nxt = i - 1
                if nxt >= 0 and not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
                for j in idx_map[arr[i]]:
                    if not visited[j]:
                        visited[j] = True
                        dq.append(j)
                idx_map[arr[i]].clear()
            steps += 1
        return -1
