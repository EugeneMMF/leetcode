
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp_prev[a_count][l_streak] stores the number of valid records of length i-1
        # a_count: 0 or 1 (number of 'A's encountered so far)
        # l_streak: 0, 1, or 2 (number of consecutive 'L's at the end)

        # Initialize for records of length 0 (empty string):
        # One way to have 0 'A's and 0 consecutive 'L's (the empty string itself).
        # All other states are 0.
        dp_prev = [[0] * 3 for _ in range(2)]
        dp_prev[0][0] = 1

        # Iterate to build records from length 1 up to n
        for _ in range(1, n + 1):
            # dp_curr will store the counts for records of the current length
            dp_curr = [[0] * 3 for _ in range(2)]

            # Iterate through all possible previous states (a_count, l_streak)
            for a_count in range(2):
                for l_streak in range(3):
                    # If there are no ways to reach this previous state, skip
                    if dp_prev[a_count][l_streak] == 0:
                        continue

                    current_ways = dp_prev[a_count][l_streak]

                    # Option 1: Add 'P' (Present)
                    # Adding 'P' does not change 'A' count and resets 'L' streak to 0.
                    dp_curr[a_count][0] = (dp_curr[a_count][0] + current_ways) % MOD

                    # Option 2: Add 'L' (Late)
                    # Adding 'L' does not change 'A' count.
                    # 'L' streak increases by 1, but cannot exceed 2.
                    if l_streak < 2:
                        dp_curr[a_count][l_streak + 1] = (dp_curr[a_count][l_streak + 1] + current_ways) % MOD

                    # Option 3: Add 'A' (Absent)
                    # Adding 'A' increments 'A' count.
                    # Can only add 'A' if 'A' count was previously 0.
                    # Adding 'A' resets 'L' streak to 0.
                    if a_count == 0:
                        dp_curr[1][0] = (dp_curr[1][0] + current_ways) % MOD
            
            # After calculating all states for the current length, update dp_prev for the next iteration
            dp_prev = dp_curr

        # Sum up all valid states for records of length n
        total_ways = 0
        for a_count in range(2):
            for l_streak in range(3):
                total_ways = (total_ways + dp_prev[a_count][l_streak]) % MOD
        
        return total_ways

