class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_palindromes = 0

        def expand_around_center(l, r):
            palindromes_from_center = 0
            while l >= 0 and r < n and s[l] == s[r]:
                palindromes_from_center += 1
                l -= 1
                r += 1
            return palindromes_from_center

        for i in range(n):
            total_palindromes += expand_around_center(i, i)
            total_palindromes += expand_around_center(i, i + 1)
            
        return total_palindromes
