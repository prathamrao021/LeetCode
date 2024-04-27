class Solution():
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_1 = []
        row_2 = []
        row_3 = []
        row_4 = []
        row_5 = []
        row_6 = []
        row_7 = []
        row_8 = []
        row_9 = []

        column_1 = []
        column_2 = []
        column_3 = []
        column_4 = []
        column_5 = []
        column_6 = []
        column_7 = []
        column_8 = []
        column_9 = []

        box_1 = []
        box_2 = []
        box_3 = []
        box_4 = []
        box_5 = []
        box_6 = []
        box_7 = []
        box_8 = []
        box_9 = []
        for i in range(len(board)):
            if i//3 == 0:
                if i%3 == 0:
                    row_1 = board[i]
                if i%3 == 1:
                    row_2 = board[i]
                if i%3 == 2:
                    row_3 = board[i]
            if i//3 == 1:
                if i%3 == 0:
                    row_4 = board[i]
                if i%3 == 1:
                    row_5 = board[i]
                if i%3 == 2:
                    row_6 = board[i]
            if i//3 == 2:
                if i%3 == 0:
                    row_7 = board[i]
                if i%3 == 1:
                    row_8 = board[i]
                if i%3 == 2:
                    row_9 = board[i]

            for j in range(len(board[i])):
                if j//3 == 0:
                    if j%3 == 0:
                        column_1.append(board[i][j])
                    if j%3 == 1:
                        column_2.append(board[i][j])
                    if j%3 == 2:
                        column_3.append(board[i][j])
                if j//3 == 1:
                    if j%3 == 0:
                        column_4.append(board[i][j])
                    if j%3 == 1:
                        column_5.append(board[i][j])
                    if j%3 == 2:
                        column_6.append(board[i][j])
                if j//3 == 2:
                    if j%3 == 0:
                        column_7.append(board[i][j])
                    if j%3 == 1:
                        column_8.append(board[i][j])
                    if j%3 == 2:
                        column_9.append(board[i][j])
                
                if i <= 2 and j <= 2:
                    box_1.append(board[i][j])
                if i <= 2 and j <= 5 and j > 2:
                    box_2.append(board[i][j])
                if i <= 2 and j <= 8 and j > 5:
                    box_3.append(board[i][j])
                
                if i > 2 and i <= 5 and j <= 2:
                    box_4.append(board[i][j])
                if i > 2 and i <= 5 and j <= 5 and j > 2:
                    box_5.append(board[i][j])
                if i > 2 and i <= 5 and j <= 8 and j > 5:
                    box_6.append(board[i][j])

                if i > 5 and i <= 8 and j <= 2:
                    box_7.append(board[i][j])
                if i > 5 and i <= 8 and j <= 5 and j > 2:
                    box_8.append(board[i][j])
                if i > 5 and i <= 8 and j <= 8 and j > 5:
                    box_9.append(board[i][j])
        
        all_box = [box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9]
        all_row = [row_1,row_2,row_3,row_4,row_5,row_6,row_7,row_8,row_9]
        all_column = [column_1,column_2,column_3,column_4,
        column_5,column_6,column_7,column_8,column_9]

        print(row_3)
        for i in all_box:
            temp_set = set()
            for j in i:
                if j.isnumeric() and j in temp_set:
                    return False
                elif j.isnumeric() and j not in temp_set:
                    temp_set.add(j)

        for i in all_row:
            temp_set = set()
            for j in i:
                if j.isnumeric() and j in temp_set:
                    return False
                elif j.isnumeric() and j not in temp_set:
                    temp_set.add(j)
        
        for i in all_column:
            temp_set = set()
            for j in i:
                if j.isnumeric() and j in temp_set:
                    return False
                elif j.isnumeric() and j not in temp_set:
                    temp_set.add(j)
        return True
s = Solution()
# inp = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]
# inp = [
#     ["8","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]

inp = [
    [".",".",".",".",".","6",".",".","."],
    [".",".",".",".",".","1",".",".","."],
    ["4","5",".",".",".","3",".","3","9"],
    [".",".",".",".",".",".",".",".","."],
    [".","9",".",".",".",".",".",".","."],
    [".",".",".",".","3",".",".",".","6"],
    ["8",".",".",".",".",".","4",".","."],
    ["9",".",".",".",".",".",".","1","."],
    [".",".",".",".",".",".","8",".","."]]
j = s.isValidSudoku(inp)
print(j)