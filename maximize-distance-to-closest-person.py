class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_dist = 0
        prev_person = -1

        for i in range(n):
            if seats[i] == 1:
                if prev_person == -1:
                    max_dist = max(max_dist, i)
                else:
                    max_dist = max(max_dist, (i - prev_person) // 2)
                prev_person = i

        max_dist = max(max_dist, n - 1 - prev_person)
        return max_dist
