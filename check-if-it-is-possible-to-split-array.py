class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        pref = [0]*(n+1)
        for i,v in enumerate(nums,1):
            pref[i] = pref[i-1]+v
        def sub(i,j):
            return pref[j+1]-pref[i]
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                for k in range(i, j):
                    left_len = k-i+1
                    right_len = j-k
                    left_good = left_len==1 or sub(i,k)>=m
                    right_good = right_len==1 or sub(k+1,j)>=m
                    if left_good and right_good and dp[i][k] and dp[k+1][j]:
                        dp[i][j] = True
                        break
        return dp[0][n-1]