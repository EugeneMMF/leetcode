class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        n = len(s1)
        even1 = [0] * 26
        odd1 = [0] * 26
        even2 = [0] * 26
        odd2 = [0] * 26
        for i in range(n):
            c1 = ord(s1[i]) - 97
            c2 = ord(s2[i]) - 97
            if i % 2 == 0:
                even1[c1] += 1
                even2[c2] += 1
            else:
                odd1[c1] += 1
                odd2[c2] += 1
        return even1 == even2 and odd1 == odd2
