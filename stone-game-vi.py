class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        combined = [a + b for a, b in zip(aliceValues, bobValues)]
        idx = sorted(range(len(combined)), key=lambda i: combined[i], reverse=True)
        diff = 0
        for turn, i in enumerate(idx):
            if turn % 2 == 0:
                diff += aliceValues[i]
            else:
                diff -= bobValues[i]
        if diff > 0:
            return 1
        if diff < 0:
            return -1
        return 0
