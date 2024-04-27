class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []
        for i in range(m):
            cols = []
            for j in range(n): 
                cols.append(0)
            dp.append(cols)
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    if (j == 0 and i == 0):
                        dp[i][j] = 1
                    elif j == 0 and i != 0:
                        dp[i][j] = dp[i-1][j]
                    elif j != 0 and i == 0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return (dp[m-1][n-1])

s = Solution()
print(s.uniquePathsWithObstacles([[1,0]]))