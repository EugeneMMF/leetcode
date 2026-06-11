class Solution:
    def distMoney(self, money: int, children: int) -> int:
        max_k = min(children, money // 8)
        for k in range(max_k, -1, -1):
            r = children - k
            M = money - 8 * k
            if M < r:
                continue
            if r == 0:
                if M == 0:
                    return k
                continue
            if r == 1:
                if M >= 1 and M != 4:
                    return k
                continue
            if r >= 2:
                return k
        return -1