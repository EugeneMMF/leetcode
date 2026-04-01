class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        
        dp = {}
        
        arr_set = set(arr)
        
        for x in arr:
            dp[x] = 1
            
            for y in arr:
                if y * y > x:
                    break
                
                if x % y == 0:
                    z = x // y
                    
                    if z in arr_set:
                        
                        if y == z:
                            dp[x] = (dp[x] + dp[y] * dp[z]) % MOD
                        else:
                            dp[x] = (dp[x] + 2 * dp[y] * dp[z]) % MOD
                            
        total_trees = 0
        for val in dp.values():
            total_trees = (total_trees + val) % MOD
            
        return total_trees
