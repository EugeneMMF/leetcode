from collections import deque

class Solution:
    def finalString(self, s: str) -> str:
        dq = deque()
        rev = False
        for ch in s:
            if ch == 'i':
                rev = not rev
            else:
                if rev:
                    dq.appendleft(ch)
                else:
                    dq.append(ch)
        if rev:
            dq.reverse()
        return ''.join(dq)
