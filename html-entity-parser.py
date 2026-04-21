class Solution:
    def entityParser(self, text: str) -> str:
        mapping = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        i = 0
        n = len(text)
        res = []
        while i < n:
            if text[i] == '&':
                matched = False
                for ent, ch in mapping.items():
                    if text.startswith(ent, i):
                        res.append(ch)
                        i += len(ent)
                        matched = True
                        break
                if not matched:
                    res.append('&')
                    i += 1
            else:
                res.append(text[i])
                i += 1
        return ''.join(res)
