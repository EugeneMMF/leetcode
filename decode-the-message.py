class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        seen = set()
        idx = 0
        for c in key:
            if c == ' ' or c in seen:
                continue
            mapping[c] = chr(ord('a') + idx)
            seen.add(c)
            idx += 1
            if idx == 26:
                break
        res = []
        for c in message:
            if c == ' ':
                res.append(' ')
            else:
                res.append(mapping[c])
        return ''.join(res)