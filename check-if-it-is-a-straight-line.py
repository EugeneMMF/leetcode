class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0][0], coordinates[0][1]
        x1, y1 = coordinates[1][0], coordinates[1][1]

        dx_ref = x1 - x0
        dy_ref = y1 - y0

        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i][0], coordinates[i][1]
            if (yi - y0) * dx_ref != dy_ref * (xi - x0):
                return False
        
        return True

