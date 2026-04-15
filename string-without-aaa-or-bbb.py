class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if len(res) >= 2 and res[-1] == res[-2] == 'a':
                res.append('b')
                b -= 1
            elif len(res) >= 2 and res[-1] == res[-2] == 'b':
                res.append('a')
                a -= 1
            else:
                if a >= b:
                    if a > 0:
                        res.append('a')
                        a -= 1
                    else:
                        res.append('b')
                        b -= 1
                else:
                    if b > 0:
                        res.append('b')
                        b -= 1
                    else:
                        res.append('a')
                        a -= 1
        return ''.join(res)
