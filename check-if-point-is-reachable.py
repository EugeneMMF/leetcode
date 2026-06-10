class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        if targetX == 1 or targetY == 1:
            return True
        if targetX == targetY:
            return (targetX & (targetX - 1)) == 0
        while targetX > 1 and targetY > 1:
            if targetX > targetY:
                targetX %= targetY
                if targetX == 0:
                    targetX = targetY
            else:
                targetY %= targetX
                if targetY == 0:
                    targetY = targetX
            if targetX == targetY:
                return (targetX & (targetX - 1)) == 0
        return True