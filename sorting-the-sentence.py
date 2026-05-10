class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        indexed = [(int(w[-1]) - 1, w[:-1]) for w in words]
        indexed.sort(key=lambda x: x[0])
        return ' '.join(word for _, word in indexed)