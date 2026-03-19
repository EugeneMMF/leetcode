
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.radius_sq = radius * radius

    def randPoint(self) -> [float]:
        while True:
            x = random.uniform(self.x_center - self.radius, self.x_center + self.radius)
            y = random.uniform(self.y_center - self.radius, self.y_center + self.radius)

            dist_sq = (x - self.x_center)**2 + (y - self.y_center)**2

            if dist_sq <= self.radius_sq:
                return [x, y]

