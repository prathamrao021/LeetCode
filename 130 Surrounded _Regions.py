class Solution:

    def dfs(self, board, r, c):
        num_rows = len(board)
        num_cols = len(board[0])
        
        board[r][c] = "#"

        if r+1 < num_rows-1 and board[r+1][c] == "O":
            self.dfs(board, r+1, c)
        if r-1 > 0 and board[r-1][c] == "O":
            self.dfs(board, r-1, c)
        if c+1 < num_cols-1 and board[r][c+1] == "O":
            self.dfs(board, r, c+1)
        if c-1 > 0 and board[r][c-1] == "O":
            self.dfs(board, r, c-1)

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        ele_queue = []
        for row in range(len(board)):
            for ele in range(len(board[0])):
                if (row == 0 or row == len(board)-1 or ele == 0 or ele == len(board[0])-1) and board[row][ele] == "O":
                    # board[row][ele] = "#"
                    ele_queue.append([row,ele])
        for pos in ele_queue:
            self.dfs(board,pos[0],pos[1])

        for row in range(len(board)):
            for ele in range(len(board[0])):
                if board[row][ele] == "O":
                    board[row][ele] = 'X'
                elif board[row][ele] == "#":
                    board[row][ele] = 'O'
        

            

if __name__ == "__main__":
    s = Solution()

    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

    board = s.solve(board)
        