class Solution:
    def modifyString(self, s: str) -> str:
        s_list = list(s)
        n = len(s_list)
        for i in range(n):
            if s_list[i] == '?':
                for ch in ('a', 'b', 'c'):
                    prev = s_list[i-1] if i > 0 else ''
                    nxt = s_list[i+1] if i+1 < n else ''
                    if ch != prev and ch != nxt:
                        s_list[i] = ch
                        break
        return ''.join(s_list)
