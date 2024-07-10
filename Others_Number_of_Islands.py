class Solution:
    def dfs(self, matrix, r_th, c_th):
        row_num = len(matrix)
        col_num = len(matrix[0])

        if (r_th >= row_num or r_th < 0 or c_th >= col_num or c_th < 0 or matrix[r_th][c_th] == 0):
            return
        
        matrix[r_th][c_th] = 0
        self.dfs(matrix, r_th+1, c_th)
        self.dfs(matrix, r_th, c_th+1)
        self.dfs(matrix, r_th-1, c_th)
        self.dfs(matrix, r_th, c_th-1)
        

    def n_island(self,matrix):
        number_of_islands = 0
        if len(matrix) == 0:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    number_of_islands += 1
                    self.dfs(matrix, i, j)

        return number_of_islands

if __name__ == "__main__":
    s = Solution()

    # matrix = [[0,0,0,1],[1,1,1,0],[0,0,1,1],[1,0,0,1]]
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    k = s.n_island(grid)
    print(k)