class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        n2 = len(str2)
        for ch in str1:
            if j < n2:
                target = str2[j]
                if ch == target or (ch == 'z' and target == 'a') or (ch != 'z' and chr(ord(ch)+1) == target):
                    j += 1
        return j == n2