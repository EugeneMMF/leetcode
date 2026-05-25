class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n <= 1:
            return 0
        if n == 2:
            return 1
        stockPrices.sort(key=lambda x: x[0])
        count = 1
        p0 = stockPrices[0]
        p1 = stockPrices[1]
        for i in range(2, n):
            p2 = stockPrices[i]
            if (p1[0] - p0[0]) * (p2[1] - p1[1]) != (p1[1] - p0[1]) * (p2[0] - p1[0]):
                count += 1
                p0 = p1
            p1 = p2
        return count
