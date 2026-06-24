class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist = 0
        while mainTank > 0:
            if mainTank >= 5:
                mainTank -= 5
                dist += 50
                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                dist += mainTank * 10
                mainTank = 0
        return dist
