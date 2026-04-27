class Solution:
    def maximumRequests(self, n, requests):
        m = len(requests)
        ans = 0
        for mask in range(1 << m):
            cnt = mask.bit_count()
            if cnt <= ans:
                continue
            bal = [0] * n
            for i in range(m):
                if mask >> i & 1:
                    f, t = requests[i]
                    bal[f] -= 1
                    bal[t] += 1
            if all(x == 0 for x in bal):
                ans = cnt
        return ans
