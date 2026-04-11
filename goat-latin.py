class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        res = []
        for i, w in enumerate(words, 1):
            if w[0] in vowels:
                cur = w + 'ma'
            else:
                cur = w[1:] + w[0] + 'ma'
            cur += 'a' * i
            res.append(cur)
        return ' '.join(res)
