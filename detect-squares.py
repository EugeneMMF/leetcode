class DetectSquares:

    def __init__(self):
        self.counts = {}

    def add(self, point: List[int]) -> None:
        key = (point[0], point[1])
        self.counts[key] = self.counts.get(key, 0) + 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        total = 0
        for (x1, y1), c1 in self.counts.items():
            dx = x1 - x0
            dy = y1 - y0
            if dx != 0 and abs(dx) == abs(dy):
                c2 = self.counts.get((x0, y1), 0)
                c3 = self.counts.get((x1, y0), 0)
                total += c1 * c2 * c3
        return total

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)