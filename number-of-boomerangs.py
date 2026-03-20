from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        n = len(points)
        boomerang_count = 0

        for i in range(n):
            p1 = points[i]
            distance_counts = defaultdict(int)

            for j in range(n):
                if i == j:
                    continue

                p2 = points[j]

                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]

                squared_distance = dx*dx + dy*dy
                distance_counts[squared_distance] += 1

            for count in distance_counts.values():
                boomerang_count += count * (count - 1)

        return boomerang_count