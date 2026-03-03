class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Pad nums with 1s at both ends to handle boundary conditions
        # Original nums[i] will be nums_padded[i+1]
        # The virtual balloons at the boundaries are at index 0 and n+1
        nums_padded = [1] + nums + [1]
        
        # N is the length of the padded array
        N = len(nums_padded)
        
        # dp[i][j] will store the maximum coins collected by bursting
        # all balloons strictly between index i and index j in nums_padded.
        # This implies that nums_padded[i] and nums_padded[j] are the last
        # two balloons remaining unburst in this subproblem.
        dp = [[0] * N for _ in range(N)]
        
        # Iterate over the length of the subarray (excluding the boundary 1s)
        # 'length' here represents (j - i), the distance between the two walls.
        # It ranges from 2 (meaning one balloon between i and j) to N-1 (all original balloons).
        for length in range(2, N):
            # Iterate over the starting index 'i' of the left wall
            # 'i' can go from 0 up to N - length - 1
            # (such that j = i + length does not exceed N-1)
            for i in range(N - length):
                # Calculate the index 'j' of the right wall
                j = i + length
                
                # Iterate over 'k', which is the index of the last balloon to burst
                # within the segment nums_padded[i+1 ... j-1].
                # When nums_padded[k] is burst last, its immediate neighbors are nums_padded[i] and nums_padded[j].
                for k in range(i + 1, j):
                    # Calculate coins for this choice of 'k' as the last balloon:
                    # dp[i][k] -> coins from bursting balloons in the left subsegment (i, k)
                    # dp[k][j] -> coins from bursting balloons in the right subsegment (k, j)
                    # nums_padded[i] * nums_padded[k] * nums_padded[j] -> coins from bursting nums_padded[k] itself
                    current_coins = dp[i][k] + dp[k][j] + nums_padded[i] * nums_padded[k] * nums_padded[j]
                    
                    # Update dp[i][j] with the maximum coins found so far
                    dp[i][j] = max(dp[i][j], current_coins)
                    
        # The result is the maximum coins for bursting all original balloons,
        # which corresponds to the segment from index 0 to N-1 in nums_padded.
        return dp[0][N - 1]

