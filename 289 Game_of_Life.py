class Solution:
    def calculate(self, board, r, c):
        live_count = 0
        for i in ([-1,0,1]):
            for j in ([-1,0,1]):
                if i == 0 and j == 0:
                    continue
                elif r+i < 0 or c+j < 0 or r+i > len(board)-1 or c+j > len(board[0])-1:
                    continue
                elif board[r+i][c+j] == 1 or board[r+i][c+j] == -1:
                    live_count += 1
        
        if board[r][c] == 1:
            if live_count < 2:
                board[r][c] = -1
            elif 2 >= live_count <= 3:
                board[r][c] == 1
            elif live_count > 3:
                board[r][c] = -1
        elif board[r][c] == 0:
            if live_count == 3:
                board[r][c] = 2
        return board
        

    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # -1 as before it was alive but now it is dead
        # decisions are made on the basis of the before conditions
        # 2 as before it was dead but now it is alive
        for i in range(len(board)):
            for j in range(len(board[0])):
                board = self.calculate(board, i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
        return board

if __name__ == "__main__":
    s = Solution()
    s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
        