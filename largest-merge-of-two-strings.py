class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        n1, n2 = len(word1), len(word2)
        res = []
        while i < n1 or j < n2:
            if i == n1:
                res.append(word2[j]); j += 1
            elif j == n2:
                res.append(word1[i]); i += 1
            else:
                if word1[i:] >= word2[j:]:
                    res.append(word1[i]); i += 1
                else:
                    res.append(word2[j]); j += 1
        return ''.join(res)
