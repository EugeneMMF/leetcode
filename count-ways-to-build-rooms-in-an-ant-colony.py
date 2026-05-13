class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9+7
        n = len(prevRoom)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[prevRoom[i]].append(i)
        size = [0]*n
        stack = [(0, 0)]  # (node, state) 0=pre,1=post
        while stack:
            node, state = stack.pop()
            if state == 0:
                stack.append((node, 1))
                for c in children[node]:
                    stack.append((c, 0))
            else:
                total = 0
                for c in children[node]:
                    total += size[c]
                size[node] = total + 1
        fac = [1]*(n+1)
        for i in range(1, n+1):
            fac[i] = fac[i-1]*i%MOD
        invfac = [1]*(n+1)
        invfac[n] = pow(fac[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfac[i-1] = invfac[i]*i%MOD
        res = 1
        for node in range(n):
            total = size[node]-1
            res = res*fac[total]%MOD
            for c in children[node]:
                res = res*invfac[size[c]]%MOD
        return res