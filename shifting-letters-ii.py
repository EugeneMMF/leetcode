class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for a, b, c in shifts:
            delta = 1 if c == 1 else -1
            diff[a] += delta
            if b + 1 < n:
                diff[b + 1] -= delta
        res = []
        cur = 0
        for i, ch in enumerate(s):
            cur += diff[i]
            shift = (cur % 26 + 26) % 26
            res.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        return ''.join(res)
