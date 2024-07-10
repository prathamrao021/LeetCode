class Solution:
    def dfs(self, grid):
        if len(self.bfs_queue) == 0:
            return
        x = self.bfs_queue.pop(0)
        r,c = x[0],x[1]
                                
        max_row = len(grid)
        max_col = len(grid[0])
        self.visited.append([r,c])

        self.perimeter += 4
        if (r-1 >= 0) and grid[r-1][c] == 1:
            self.perimeter -=  1
            if [r-1,c] not in self.visited and [r-1,c] not in self.bfs_queue:
                self.bfs_queue.append([r-1,c])
        if (c-1 >= 0) and grid[r][c-1] == 1:
            self.perimeter -=  1
            if [r,c-1] not in self.visited  and [r,c-1] not in self.bfs_queue:
                self.bfs_queue.append([r,c-1])
        if (r+1 < max_row) and grid[r+1][c] == 1:
            self.perimeter -=  1
            if [r+1,c] not in self.visited  and [r+1,c] not in self.bfs_queue:
                self.bfs_queue.append([r+1,c])
        if (c+1 < max_col) and grid[r][c+1] == 1:
            self.perimeter -=  1
            if [r,c+1] not in self.visited  and [r,c+1] not in self.bfs_queue:
                self.bfs_queue.append([r,c+1])
        
        if len(self.bfs_queue) == 0:
            return
        else:
            self.dfs(grid)

        # perimeter = self.dfs(grid, r+1, c, perimeter-1)
        # perimeter = self.dfs(grid, r-1, c, perimeter-1)
        # perimeter = self.dfs(grid, r, c+1, perimeter-1)
        # perimeter = self.dfs(grid, r, c-1, perimeter-1)

    def islandPerimeter(self, grid) -> int:
        self.perimeter = 0
        self.bfs_queue = []
        self.visited = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and grid[i][j] not in self.visited:
                    self.bfs_queue.append([i,j])
        
        self.dfs(grid)
        # while self.bfs_queue:
            
        return(self.perimeter)




if __name__ == "__main__":
    s = Solution()
    k = s.islandPerimeter([[1,1],[1,1]])
    print(k)

# --------------

# grid = [[0,1,0,0],
#         [1,1,1,0],
#         [0,1,0,0],
#         [1,1,0,0]]
# perimeter = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == 1:
#             perimeter += 4
#             if (i-1 >= 0) and grid[i-1][j] == 1:
#                 perimeter -= 1
#             if (i+1 < len(grid)) and grid[i+1][j] == 1:
#                 perimeter -= 1
#             if (j -1 >= 0) and grid[i][j-1] == 1:
#                 perimeter -= 1
#             if (j+1 < len(grid[0])) and grid[i][j+1] == 1:
#                 perimeter -= 1
        
# print(perimeter)
         