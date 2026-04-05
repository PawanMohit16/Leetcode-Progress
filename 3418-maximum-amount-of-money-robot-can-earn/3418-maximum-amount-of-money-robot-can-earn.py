class Solution:
    def maximumAmount(self, coins):
        n, m = len(coins), len(coins[0])
        
        dp = [[[-10**9] * 3 for _ in range(m)] for _ in range(n)]
        
        dp[0][0][0] = coins[0][0] 
        dp[0][0][1] = 0           
        dp[0][0][2] = 0            
        
        for i in range(n):
            for j in range(m):
                for k in range(3):
                    if i > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                        if k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])

                    if j > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])
                        if k > 0:
                            dp[i][j][k] = max(dp[i][j][k],dp[i][j-1][k-1])

        return max(dp[n-1][m-1])