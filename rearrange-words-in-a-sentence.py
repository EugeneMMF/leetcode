class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        lower = [w.lower() for w in words]
        sorted_words = sorted(lower, key=len)
        if sorted_words:
            sorted_words[0] = sorted_words[0].capitalize()
        return ' '.join(sorted_words)
