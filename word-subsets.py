from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        req = [0] * 26
        for w in words2:
            cnt = [0] * 26
            for ch in w:
                idx = ord(ch) - 97
                cnt[idx] += 1
                if cnt[idx] > req[idx]:
                    req[idx] = cnt[idx]
        res = []
        for w in words1:
            cnt = [0] * 26
            for ch in w:
                cnt[ord(ch) - 97] += 1
            for i in range(26):
                if cnt[i] < req[i]:
                    break
            else:
                res.append(w)
        return res
