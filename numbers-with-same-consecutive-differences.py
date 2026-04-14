class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        cur = [i for i in range(1, 10)]
        for _ in range(n - 1):
            nxt = []
            for num in cur:
                last = num % 10
                add = last + k
                sub = last - k
                if add < 10:
                    nxt.append(num * 10 + add)
                if k != 0 and sub >= 0:
                    nxt.append(num * 10 + sub)
            cur = nxt
        return cur
