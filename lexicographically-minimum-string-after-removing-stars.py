class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        letter_lists = [[] for _ in range(26)]
        deleted = [False] * n
        for i, ch in enumerate(s):
            if ch == '*':
                for idx in range(26):
                    if letter_lists[idx]:
                        pos = letter_lists[idx].pop()
                        deleted[pos] = True
                        break
            else:
                letter_lists[ord(ch) - 97].append(i)
        res = []
        for i, ch in enumerate(s):
            if ch != '*' and not deleted[i]:
                res.append(ch)
        return ''.join(res)
