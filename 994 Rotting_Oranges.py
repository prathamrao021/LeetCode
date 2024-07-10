class Solution:    
    def orangesRotting(self, grid) -> int:
        self.time = -1
        self.queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.queue.append([i,j])
        
        count = len(self.queue)
        while len(self.queue) != 0:
            x = self.queue.pop(0)
            r,c = x[0], x[1]
            count -= 1
            grid[r][c] = 2
            if r+1 < len(grid) and grid[r+1][c] == 1 and [r+1,c] not in self.queue:
                self.queue.append([r+1,c])
            if c+1 < len(grid[0]) and grid[r][c+1] == 1 and [r,c+1] not in self.queue:
                self.queue.append([r,c+1])
            if r-1 >= 0 and grid[r-1][c] == 1 and [r-1,c] not in self.queue:
                self.queue.append([r-1,c])
            if c-1 >= 0 and grid[r][c-1] == 1 and [r,c-1] not in self.queue:
                self.queue.append([r,c-1])
            if count == 0:
                self.time += 1
                count = len(self.queue)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        if self.time == -1:
            return 0
        return self.time

if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2,2],[1,1],[0,0],[2,0]]))