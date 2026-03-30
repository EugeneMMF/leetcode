class WordFilter:

    def __init__(self, words: list[str]):
        self.memo = {}
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[0:j]
                for k in range(len(word) + 1):
                    suffix = word[len(word) - k:len(word)]
                    self.memo[(prefix, suffix)] = i

    def f(self, pref: str, suff: str) -> int:
        return self.memo.get((pref, suff), -1)
