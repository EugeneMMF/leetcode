class Solution:
    def oddString(self, words: List[str]) -> str:
        def diff(word):
            return tuple(ord(word[i+1]) - ord(word[i]) for i in range(len(word)-1))
        d0 = diff(words[0])
        d1 = diff(words[1])
        d2 = diff(words[2])
        if d0 == d1:
            majority = d0
        elif d0 == d2:
            majority = d0
        else:
            majority = d1
        for w in words:
            if diff(w) != majority:
                return w
