class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        best = -1
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            runs = []
            i = 0
            while i < n:
                if s[i] == ch:
                    j = i
                    while j < n and s[j] == ch:
                        j += 1
                    runs.append(j - i)
                    i = j
                else:
                    i += 1
            if not runs:
                continue
            max_run = max(runs)
            for l in range(1, max_run + 1):
                total = 0
                for r in runs:
                    if r >= l:
                        total += r - l + 1
                if total >= 3 and l > best:
                    best = l
        return best
