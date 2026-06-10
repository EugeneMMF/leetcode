class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        s_has_one = '1' in s
        t_has_one = '1' in target
        return s_has_one == t_has_one