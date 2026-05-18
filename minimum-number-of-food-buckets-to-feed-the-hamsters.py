class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        s = list(hamsters)
        n = len(s)
        count = 0
        for i in range(n):
            if s[i] == 'H':
                fed = False
                if i > 0 and s[i - 1] == 'B':
                    fed = True
                if i + 1 < n and s[i + 1] == 'B':
                    fed = True
                if fed:
                    continue
                if i + 1 < n and s[i + 1] == '.':
                    s[i + 1] = 'B'
                    count += 1
                    continue
                if i > 0 and s[i - 1] == '.':
                    s[i - 1] = 'B'
                    count += 1
                    continue
                return -1
        return count
