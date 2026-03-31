class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # dp[i] will store the minimum cost to reach city i considering the current number of stops.
        # Initialize dp array with infinity for all cities except the source.
        # dp[city] represents the minimum cost to reach 'city' using at most 'current_loop_iteration - 1' stops.
        dp = [float('inf')] * n
        dp[src] = 0

        # min_price will store the overall minimum price found to reach the destination
        # across all valid numbers of stops (from 0 to k).
        min_price = float('inf')

        # The loop runs for `k + 1` iterations.
        # In iteration `s` (from 0 to k):
        # We calculate the minimum costs to reach all cities using at most `s` stops.
        # 's' represents the number of stops allowed. So, `s` stops means `s + 1` segments/flights.
        for stops_allowed in range(k + 1):
            # Create a temporary dp array for the current iteration.
            # This is crucial to ensure that updates within the same iteration
            # do not use prices that were just updated in the current iteration,
            # which would effectively mean taking more than 'stops_allowed' stops in a single step.
            # `temp_dp` will hold costs for paths using at most `stops_allowed` stops.
            # It's initialized with values from `dp`, which hold costs for paths using at most `stops_allowed - 1` stops.
            temp_dp = list(dp) 

            # Iterate through all flights to update the costs.
            for fromi, toi, pricei in flights:
                # If we have a valid path to 'fromi' from the previous iteration
                # (meaning, 'fromi' was reachable with `stops_allowed - 1` stops or fewer),
                # we can potentially extend this path to 'toi'.
                if dp[fromi] != float('inf'):
                    # Update the cost to reach 'toi' using `stops_allowed` stops.
                    # We take the minimum of the current cost to 'toi' (from `stops_allowed - 1` stops)
                    # and the cost of reaching 'fromi' (with `stops_allowed - 1` stops) plus the flight price.
                    temp_dp[toi] = min(temp_dp[toi], dp[fromi] + pricei)
            
            # Update the main dp array with the costs calculated in this iteration.
            # Now, `dp` contains the minimum costs to reach each city using at most `stops_allowed` stops.
            dp = temp_dp
            
            # After each iteration, check if the destination is reachable with the current
            # maximum number of allowed stops and update min_price.
            # dp[dst] at this point holds the minimum price to reach dst using AT MOST 'stops_allowed' stops.
            min_price = min(min_price, dp[dst])
        
        # If min_price is still infinity after all iterations, it means the destination is not reachable
        # within k stops. In this case, return -1.
        return min_price if min_price != float('inf') else -1

