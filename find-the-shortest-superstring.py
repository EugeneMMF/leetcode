class Solution:
    def shortestSuperstring(self, words):
        n = len(words)
        overlap = [[0]*n for _ in range(n)]
        add = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                max_ol = min(len(words[i]), len(words[j]))
                for k in range(max_ol, -1, -1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j] = k
                        break
                add[i][j] = words[j][overlap[i][j]:]
        dp = [[""]*n for _ in range(1<<n)]
        for i in range(n):
            dp[1<<i][i] = words[i]
        for mask in range(1<<n):
            for i in range(n):
                if not (mask & (1<<i)) or dp[mask][i]=="":
                    continue
                for j in range(n):
                    if mask & (1<<j):
                        continue
                    nxt = mask | (1<<j)
                    cand = dp[mask][i] + add[i][j]
                    if dp[nxt][j]=="" or len(cand) < len(dp[nxt][j]):
                        dp[nxt][j] = cand
        full = (1<<n)-1
        ans = ""
        for i in range(n):
            cur = dp[full][i]
            if cur and (ans=="" or len(cur) < len(ans)):
                ans = cur
        return ans
