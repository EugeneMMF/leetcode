class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(word)
        ans = 0
        for i in range(n):
            mask = 0
            cons = 0
            for j in range(i, n):
                c = word[j]
                if c in vowels:
                    if c == 'a':
                        mask |= 1
                    elif c == 'e':
                        mask |= 2
                    elif c == 'i':
                        mask |= 4
                    elif c == 'o':
                        mask |= 8
                    elif c == 'u':
                        mask |= 16
                else:
                    cons += 1
                if mask == 31 and cons == k:
                    ans += 1
        return ans
