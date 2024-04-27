class Solution:
    # def lookup_except(self, board, word, ans, already_taken, i, j, index, temp_word =''):
    #     if word == temp_word:
    #         ans = True
    #         return ans
    #     try:
    #         if word == temp_word:
    #             ans = True
    #             return ans
    #         if board[i+1][j] == word[index] and [i+1,j] not in already_taken and i < len(board):
    #             temp_word += word[index]
    #             already_taken.append([i+1,j])
    #             index += 1
    #             print("lower row", temp_word)
    #             ans = self.lookup_except(board, word, ans, already_taken, i+1, j, index, temp_word)
    #             return ans
    #     except Exception as e:
    #         print(e)
    #     try:
    #         if word == temp_word:
    #             ans = True
    #             return ans
    #         if board[i-1][j] == word[index] and [i-1,j] not in already_taken and i > 0:
    #             temp_word += word[index]
    #             already_taken.append([i-1,j])
    #             index += 1
    #             print("upper row", temp_word)
    #             ans = self.lookup_except(board, word, ans, already_taken, i-1, j, index, temp_word)
    #             return ans
    #     except Exception as e:
    #         print(e)
    #     try:       
    #         if word == temp_word:
    #             ans = True
    #             return ans
    #         if board[i][j+1] == word[index] and [i,j+1] not in already_taken and j < len(board[0]):
    #             temp_word += word[index]
    #             already_taken.append([i,j+1])
    #             index += 1
    #             print("right col", temp_word)
    #             ans = self.lookup_except(board, word, ans, already_taken, i, j+1, index, temp_word)
    #             return ans
    #     except Exception as e:
    #         print(e)
    #     try:        
    #         if word == temp_word:
    #             ans = True
    #             return ans
    #         if board[i][j-1] == word[index] and [i,j-1] not in already_taken and j > 0:
    #             temp_word += word[index]
    #             already_taken.append([i,j-1])
    #             index += 1
    #             print("left col", temp_word)
    #             ans = self.lookup_except(board, word, ans, already_taken, i, j-1, index, temp_word)
    #             return ans
    #     except Exception as e:
    #         print(e)

    # def exist(self, board, word):
    #     already_taken = []
    #     ans = False
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if word[0] == board[i][j]:
    #                 ans = self.lookup_except(board, word, ans, already_taken + [[i,j]], i, j, 1, word[0])
    #                 if ans:
    #                     return ans
    #                 elif ans == None:
    #                     ans = False
    #     return ans
    
    # def check_all(self):
    #     pass

    def lookup_except(self, board, word, ans, already_taken, i, j, index, temp_word):
        if temp_word == word:
            ans = True
            return ans
        for k in [-1,1]:
            if i+k < len(board) and i+k >= 0 and board[i+k][j] == word[index] and [i+k,j] not in already_taken:
                # already_taken.append([i-k,j])
                # temp_word += word[index]
                # index += 1
                ans = self.lookup_except(board, word, ans, already_taken+[[i+k,j]], i+k, j, index+1, temp_word+word[index])
            if j+k < len(board[0]) and j+k >= 0 and board[i][j+k] == word[index] and [i,j+k] not in already_taken:
                # already_taken.append([i,j-k])
                # temp_word += word[index]
                # index += 1
                ans = self.lookup_except(board, word, ans, already_taken+[[i,j+k]], i, j+k, index+1, temp_word+word[index])
        return ans
    def exist(self, board, word):
        already_taken = []
        ans = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    ans = self.lookup_except(board, word, ans, already_taken + [[i,j]], i, j, 1, word[0])
                    if ans:
                        return ans
        return ans
if __name__ == "__main__":
    s = Solution()
    print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))