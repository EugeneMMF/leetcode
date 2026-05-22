class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))
        evens = sorted([d for d in digits if int(d) % 2 == 0], reverse=True)
        odds = sorted([d for d in digits if int(d) % 2 == 1], reverse=True)
        res = []
        e_idx = 0
        o_idx = 0
        for d in digits:
            if int(d) % 2 == 0:
                res.append(evens[e_idx])
                e_idx += 1
            else:
                res.append(odds[o_idx])
                o_idx += 1
        return int(''.join(res))
