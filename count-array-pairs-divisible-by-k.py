class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if k == 1:
            n = len(nums)
            return n * (n - 1) // 2
        primes = []
        exps = []
        temp = k
        p = 2
        while p * p <= temp:
            if temp % p == 0:
                cnt = 0
                while temp % p == 0:
                    temp //= p
                    cnt += 1
                primes.append(p)
                exps.append(cnt)
            p += 1 if p == 2 else 2
        if temp > 1:
            primes.append(temp)
            exps.append(1)
        m = len(primes)
        masks = []
        def gen(idx, cur):
            if idx == m:
                masks.append(tuple(cur))
                return
            for e in range(exps[idx] + 1):
                cur.append(e)
                gen(idx + 1, cur)
                cur.pop()
        gen(0, [])
        mask_index = {mask: i for i, mask in enumerate(masks)}
        M = len(masks)
        adj = [[] for _ in range(M)]
        for i in range(M):
            mi = masks[i]
            for j in range(M):
                mj = masks[j]
                ok = True
                for a, b, req in zip(mi, mj, exps):
                    if a + b < req:
                        ok = False
                        break
                if ok:
                    adj[i].append(j)
        counts = [0] * M
        ans = 0
        for num in nums:
            val = num
            exps_num = []
            for idx in range(m):
                p = primes[idx]
                cnt = 0
                while val % p == 0:
                    val //= p
                    cnt += 1
                if cnt > exps[idx]:
                    cnt = exps[idx]
                exps_num.append(cnt)
            idx_mask = mask_index[tuple(exps_num)]
            for j in adj[idx_mask]:
                ans += counts[j]
            counts[idx_mask] += 1
        return ans