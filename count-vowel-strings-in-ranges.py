from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        prefix = [0]
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        ans = []
        for l, r in queries:
            ans.append(prefix[r+1] - prefix[l])
        return ans
