class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            if res and sorted(w) == sorted(res[-1]):
                continue
            res.append(w)
        return res
