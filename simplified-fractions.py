class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for b in range(2, n + 1):
            for a in range(1, b):
                if __import__('math').gcd(a, b) == 1:
                    res.append(f"{a}/{b}")
        return res
