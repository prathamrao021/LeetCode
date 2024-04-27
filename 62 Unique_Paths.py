class Solution:
    def uniquePaths(self, m, n):
        dp = []
        for i in range(m):
            cols = []
            for j in range(n): 
                cols.append(0)
            dp.append(cols)
        
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return (dp[m-1][n-1])
