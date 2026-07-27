class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        word = [None] * L
        fixed = [False] * L
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    c = str2[j]
                    if word[pos] is None:
                        word[pos] = c
                        fixed[pos] = True
                    elif word[pos] != c:
                        return ""
        for i in range(L):
            if word[i] is None:
                word[i] = 'a'
        while True:
            changed = False
            for i in range(n):
                if str1[i] == 'F':
                    match = True
                    for j in range(m):
                        if word[i + j] != str2[j]:
                            match = False
                            break
                    if match:
                        pos_changed = False
                        for j in range(m - 1, -1, -1):
                            pos = i + j
                            if fixed[pos]:
                                continue
                            if word[pos] == str2[j]:
                                for c in 'abcdefghijklmnopqrstuvwxyz':
                                    if c != str2[j]:
                                        word[pos] = c
                                        pos_changed = True
                                        break
                                break
                        if not pos_changed:
                            return ""
                        changed = True
                        break
            if not changed:
                break
        return "".join(word)