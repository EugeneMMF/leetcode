import collections

class Solution:
    def dist_sq(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    def validSquare(self, p1, p2, p3, p4) -> bool:
        points = [p1, p2, p3, p4]
        
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(self.dist_sq(points[i], points[j]))
        
        counts = collections.Counter(distances)
        
        if len(counts) != 2:
            return False
            
        items = list(counts.items())
        
        if (items[0][1] == 4 and items[1][1] == 2):
            s_sq = items[0][0]
            d_sq = items[1][0]
        elif (items[0][1] == 2 and items[1][1] == 4):
            s_sq = items[1][0]
            d_sq = items[0][0]
        else:
            return False
            
        return s_sq > 0 and d_sq == 2 * s_sq
