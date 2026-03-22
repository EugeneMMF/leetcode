class Solution:
    def findLUSlength(self, strs: list[str]) -> int:
        def isSubsequence(s: str, t: str) -> bool:
            i = 0
            j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)

        max_uncommon_len = -1
        n = len(strs)

        for i in range(n):
            current_s = strs[i]
            is_uncommon = True
            for j in range(n):
                if i == j:
                    continue
                if isSubsequence(current_s, strs[j]):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                max_uncommon_len = max(max_uncommon_len, len(current_s))
        
        return max_uncommon_len
