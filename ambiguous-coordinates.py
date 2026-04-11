from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def gen(num: str) -> List[str]:
            res = []
            n = len(num)
            if n == 1 or num[0] != '0':
                res.append(num)
            if n > 1 and num[0] == '0':
                pass
            for i in range(1, n):
                left, right = num[:i], num[i:]
                if (len(left) > 1 and left[0] == '0') or right[-1] == '0':
                    continue
                res.append(left + '.' + right)
            return res
        inner = s[1:-1]
        ans = []
        for i in range(1, len(inner)):
            left_part, right_part = inner[:i], inner[i:]
            left_opts = gen(left_part)
            right_opts = gen(right_part)
            for l in left_opts:
                for r in right_opts:
                    ans.append(f'({l}, {r})')
        return ans
