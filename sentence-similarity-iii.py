class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()
        def check(short, long):
            m, n = len(short), len(long)
            for i in range(m + 1):
                if short[:i] == long[:i] and short[i:] == long[n - (m - i):]:
                    return True
            return False
        return check(a, b) or check(b, a)
