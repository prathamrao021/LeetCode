class Solution:
    def dfs(self,grid,r,c):
        max_row = len(grid)
        max_col = len(grid[0])

        grid[r][c] = "0"
        if r+1 < max_row and grid[r+1][c] == "1":
            self.dfs(grid,r+1,c)
        if r-1 >= 0 and grid[r-1][c] == "1":
            self.dfs(grid,r-1,c)
        if c+1 < max_col and grid[r][c+1] == "1":
            self.dfs(grid,r,c+1)
        if c-1 >= 0 and grid[r][c-1] == "1":
            self.dfs(grid,r,c-1)
        return grid
    def numIslands(self, grid) -> int:
        no_of_islands = 0
        if len(grid) == 0:
            return no_of_islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    no_of_islands += 1
                    grid = self.dfs(grid,i,j)
        return no_of_islands

if __name__ == "__main__":
    s = Solution()

    # matrix = [[0,0,0,1],[1,1,1,0],[0,0,1,1],[1,0,0,1]]
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    k = s.numIslands(grid)
    print(k)