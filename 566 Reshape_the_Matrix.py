class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        r1 = len(mat)
        c1 = len(mat[0])

        if r*c == r1*c1:
            if r == r1:
                return mat
            else:
                arr = []
                for i in range(r1):
                    for j in range(c1):
                        arr.append(mat[i][j])
                new_mat = []
                temp = []
                k = 0
                for i in range(r):
                    for j in range(c):
                        temp.append(arr[k])
                        k += 1
                    new_mat.append(temp.copy())
                    temp = []
                return new_mat
        else:
            return mat

if __name__ == "__main__":
    s = Solution()
    s.matrixReshape([[1,2],[3,4]], 1, 4)