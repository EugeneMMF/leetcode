class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for rod in rods:
            ndp = dp.copy()
            for diff, tall in dp.items():
                ndp[diff + rod] = max(ndp.get(diff + rod, 0), tall + rod)
                nd = abs(diff - rod)
                newTall = tall + max(0, rod - diff)
                ndp[nd] = max(ndp.get(nd, 0), newTall)
            dp = ndp
        return dp.get(0, 0)
