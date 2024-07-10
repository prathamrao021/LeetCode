class Solution:
    def dfs(self, matrix, r_th, c_th, curr_area):
        row_num = len(matrix)
        col_num = len(matrix[0])

        if (r_th >= row_num or r_th < 0 or c_th >= col_num or c_th < 0 or matrix[r_th][c_th] == 0):
            return curr_area
        else:
            curr_area += 1
        
        matrix[r_th][c_th] = 0
        curr_area = self.dfs(matrix, r_th+1, c_th, curr_area)
        curr_area = self.dfs(matrix, r_th, c_th+1, curr_area)
        curr_area = self.dfs(matrix, r_th-1, c_th, curr_area)
        curr_area = self.dfs(matrix, r_th, c_th-1, curr_area)
    
        return curr_area
        

    def n_island_and_max_area(self,matrix):
        number_of_islands = 0
        max_area = 0
        curr_area = 1
        if len(matrix) == 0:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    number_of_islands += 1
                    curr_area = self.dfs(matrix, i, j, curr_area)
                    max_area = max(curr_area, max_area)
                    curr_area = 0

        return max_area, number_of_islands

if __name__ == "__main__":
    s = Solution()
    matrix = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    are, k = s.n_island(matrix)
    print(are, k)