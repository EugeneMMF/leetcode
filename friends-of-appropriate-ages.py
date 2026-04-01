
class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1

        total_requests = 0

        for ageX in range(1, 121):
            if counts[ageX] == 0:
                continue

            for ageY in range(1, 121):
                if counts[ageY] == 0:
                    continue
                
                if (ageY > 0.5 * ageX + 7) and \
                   (ageY <= ageX) and \
                   not (ageY > 100 and ageX < 100):
                    
                    if ageX == ageY:
                        total_requests += counts[ageX] * (counts[ageX] - 1)
                    else:
                        total_requests += counts[ageX] * counts[ageY]
        
        return total_requests
