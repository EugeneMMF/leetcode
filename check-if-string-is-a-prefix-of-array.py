from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        curr=""
        for w in words:
            curr+=w
            if len(curr)==len(s):
                return curr==s
            if len(curr)>len(s):
                break
        return False
