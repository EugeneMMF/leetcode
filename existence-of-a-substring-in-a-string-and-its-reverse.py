class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False
        rev = s[::-1]
        rev_subs = set(rev[i:i+2] for i in range(n-1))
        for i in range(n-1):
            if s[i:i+2] in rev_subs:
                return True
        return False
