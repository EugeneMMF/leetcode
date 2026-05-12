class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        from collections import deque
        reachable = deque([0])
        for j in range(1, n):
            while reachable and reachable[0] + maxJump < j:
                reachable.popleft()
            if reachable and reachable[0] + minJump <= j and s[j] == '0':
                if j == n - 1:
                    return True
                reachable.append(j)
        return False
