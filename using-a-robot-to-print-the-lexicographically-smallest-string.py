class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suffix = [''] * n
        min_char = chr(ord('z') + 1)
        for i in range(n - 1, -1, -1):
            if s[i] < min_char:
                min_char = s[i]
            min_suffix[i] = min_char
        stack = []
        ans = []
        for i, ch in enumerate(s):
            stack.append(ch)
            while stack and (i == n - 1 or stack[-1] <= min_suffix[i + 1]):
                ans.append(stack.pop())
        return ''.join(ans)
