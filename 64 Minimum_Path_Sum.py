class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0 and i == 0:
                    continue
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return(grid[-1][-1])


if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))