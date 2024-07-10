class Solution:
    def maximalSquare(self, matrix):
        dp = [[0 for j in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(int(dp[i][j+1]),int(dp[i+1][j]),int(dp[i][j]))+1
                else:
                    dp[i+1][j+1] = int(matrix[i][j])
        max_area = 0
        for x in range(len(dp)):
            max_area = max(dp[x][-1],max_area)
        for x in range(len(dp[0])):
            max_area = max(dp[-1][x],max_area)
        return(max_area*max_area)

if __name__ == "__main__":
    s = Solution()
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    k = s.maximalSquare(matrix)
    print(k)