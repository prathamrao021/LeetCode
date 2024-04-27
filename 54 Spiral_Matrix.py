class Solution:
    def spiralOrder(self, matrix):
        left = 0
        right= 0
        up = 0
        down = 0
        ans = []
        i = 0
        j = 0
        rows = len(matrix)
        cols = len(matrix[0])
        while len(ans) != (rows*cols):
            while j != cols-down:
                ans.append(matrix[i][j])
                j+=1
            j-=1
            i+=1
            right += 1
            if(len(ans) == (rows*cols)):
                break
            while i != rows-left:
                ans.append(matrix[i][j])
                i+=1
            i-=1
            j-=1
            down += 1
            if(len(ans) == (rows*cols)):
                break
            while j != up-1:
                ans.append(matrix[i][j])
                j-=1
            j+=1
            i-=1
            left += 1
            if(len(ans) == (rows*cols)):
                break
            while i != right-1:
                ans.append(matrix[i][j])
                i-=1
            i+=1
            j+=1
            up += 1
            if(len(ans) == (rows*cols)):
                break
        return(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
