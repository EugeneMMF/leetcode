class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        i = 0
        while i < n and s[i] == 'a':
            i += 1
        if i == n:
            return s[:-1] + 'z'
        j = i
        while j < n and s[j] != 'a':
            j += 1
        lst = list(s)
        for k in range(i, j):
            lst[k] = chr(ord(lst[k]) - 1)
        return ''.join(lst)
