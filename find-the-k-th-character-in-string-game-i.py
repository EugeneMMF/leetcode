class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            nxt = ''.join(chr((ord(c) - 97 + 1) % 26 + 97) for c in word)
            word += nxt
        return word[k - 1]
