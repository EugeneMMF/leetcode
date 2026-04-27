class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_pal(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def check(s1, s2):
            i, j = 0, len(s1) - 1
            while i < j and s1[i] == s2[j]:
                i += 1
                j -= 1
            if i >= j:
                return True
            return is_pal(s1, i, j) or is_pal(s2, i, j)
        return check(a, b) or check(b, a)
