class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        count = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                ch = word[j]
                if ch not in vowels:
                    break
                seen.add(ch)
                if len(seen) == 5:
                    count += 1
        return count
