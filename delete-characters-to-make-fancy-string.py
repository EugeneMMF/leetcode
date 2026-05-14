class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        count = 0
        for ch in s:
            if not res or ch != res[-1]:
                res.append(ch)
                count = 1
            else:
                if count < 2:
                    res.append(ch)
                    count += 1
        return ''.join(res)
