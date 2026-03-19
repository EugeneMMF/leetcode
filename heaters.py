class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()

        max_radius = 0
        heater_idx = 0
        num_heaters = len(heaters)

        for house_pos in houses:
            while heater_idx < num_heaters - 1 and heaters[heater_idx+1] <= house_pos:
                heater_idx += 1
            
            dist1 = abs(heaters[heater_idx] - house_pos)
            
            dist2 = float('inf')
            if heater_idx < num_heaters - 1:
                dist2 = abs(heaters[heater_idx+1] - house_pos)
            
            min_dist_for_house = min(dist1, dist2)
            max_radius = max(max_radius, min_dist_for_house)
        
        return max_radius
