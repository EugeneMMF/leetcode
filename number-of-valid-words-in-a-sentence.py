class Solution:
    def countValidWords(self, sentence: str) -> int:
        punctuation = set('!.,')
        count = 0
        for token in sentence.split():
            if any(ch.isdigit() for ch in token):
                continue
            hyphen_count = token.count('-')
            if hyphen_count > 1:
                continue
            punct_count = sum(ch in punctuation for ch in token)
            if punct_count > 1:
                continue
            if hyphen_count == 1:
                idx = token.find('-')
                if idx == 0 or idx == len(token) - 1:
                    continue
                if not (token[idx - 1].islower() and token[idx + 1].islower()):
                    continue
            if punct_count == 1:
                if token[-1] not in punctuation:
                    continue
            if all(ch.islower() or ch in '-!.,' for ch in token):
                count += 1
        return count
