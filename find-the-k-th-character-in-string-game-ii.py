import typing

class Solution:
    def kthCharacter(self, k: int, operations: typing.List[int]) -> str:
        def helper(k, ops):
            if not ops:
                return 'a'
            last = ops[-1]
            prev = ops[:-1]
            L = 1 << len(prev)
            if k <= L:
                return helper(k, prev)
            pos = k - L
            ch = helper(pos, prev)
            if last == 0:
                return ch
            return chr((ord(ch) - 97 + 1) % 26 + 97)
        return helper(k, operations)
