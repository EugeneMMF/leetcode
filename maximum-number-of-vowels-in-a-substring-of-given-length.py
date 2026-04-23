class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v=set('aeiou')
        cur=sum(1 for c in s[:k] if c in v)
        ans=cur
        for i in range(k,len(s)):
            if s[i] in v: cur+=1
            if s[i-k] in v: cur-=1
            if cur>ans: ans=cur
        return ans
