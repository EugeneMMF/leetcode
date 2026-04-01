class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            ys.add(y1)
            ys.add(y2)
        
        sorted_ys = sorted(list(ys))
        y_map = {y: i for i, y in enumerate(sorted_ys)}
        
        count = [0] * (len(sorted_ys))
        
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, 1))
            events.append((x2, y1, y2, -1))
        
        events.sort()
        
        total_area = 0
        prev_x = 0
        
        for x, y1, y2, type in events:
            width = x - prev_x
            height = 0
            for i in range(len(sorted_ys) - 1):
                if count[i] > 0:
                    height += sorted_ys[i+1] - sorted_ys[i]
            total_area = (total_area + width * height) % MOD
            
            for i in range(len(sorted_ys) - 1):
                if sorted_ys[i] >= y1 and sorted_ys[i+1] <= y2:
                    count[i] += type
            
            prev_x = x
            
        return total_area
