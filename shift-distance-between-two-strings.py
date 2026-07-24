class Solution:
    def shiftDistance(self, s: str, t: str, nextCost, previousCost):
        INF = 10**18
        dist = [[INF]*26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for i in range(26):
            next_i = (i+1)%26
            prev_i = (i-1)%26
            dist[i][next_i] = min(dist[i][next_i], nextCost[i])
            dist[i][prev_i] = min(dist[i][prev_i], previousCost[i])
        for k in range(26):
            dk = dist[k]
            for i in range(26):
                di = dist[i]
                aik = di[k]
                if aik==INF: continue
                for j in range(26):
                    new = aik + dk[j]
                    if new < di[j]:
                        di[j] = new
        total = 0
        for a,b in zip(s,t):
            total += dist[ord(a)-97][ord(b)-97]
        return total