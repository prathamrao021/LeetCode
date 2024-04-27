class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return ([])
        i = 0
        temp = 0
        l = len(matrix)
        repeatation = 0 
        if len(matrix) <= 3:
            repeatation = 1
        elif len(matrix) > 3:
            repeatation = len(matrix) - 2
        move = l-1
        for i in range(repeatation):
            move = l-1-i
            for j in range(i,move):
                temp = matrix[i][j]
                matrix[i][j] = matrix[l-1-j][i]
                matrix[l-1-j][i] = matrix[l-1-i][l-1-j]
                matrix[l-1-i][l-1-j] = matrix[j][l-1-i]
                matrix[j][l-1-i] = temp
            repeatation -= 1
        print(matrix)
if __name__ == "__main__":
    s = Solution()
    print(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))