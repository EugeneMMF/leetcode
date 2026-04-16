class Solution:
    def longestStrChain(self, words):
        dp={}
        words.sort(key=len)
        ans=1
        for w in words:
            best=1
            for i in range(len(w)):
                prev=w[:i]+w[i+1:]
                if prev in dp:
                    cand=dp[prev]+1
                    if cand>best:
                        best=cand
            dp[w]=best
            if best>ans:
                ans=best
        return ans
