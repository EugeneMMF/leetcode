from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        case_map = {}
        devowel_map = {}
        vowels = set('aeiou')
        def devowel(word):
            return ''.join('*' if c in vowels else c for c in word)
        for w in wordlist:
            lw = w.lower()
            if lw not in case_map:
                case_map[lw] = w
            dw = devowel(lw)
            if dw not in devowel_map:
                devowel_map[dw] = w
        res = []
        for q in queries:
            if q in exact:
                res.append(q)
                continue
            lq = q.lower()
            if lq in case_map:
                res.append(case_map[lq])
                continue
            dq = devowel(lq)
            if dq in devowel_map:
                res.append(devowel_map[dq])
                continue
            res.append("")
        return res
