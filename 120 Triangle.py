class Solution:
    def minimumTotal(self, triangle):
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if i == j:
                    triangle[i][j] += triangle[i-1][j-1]
                elif j == 0:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])

if __name__ == "__main__":
    s = Solution()
    k = s.minimumTotal([[-1],[3,2],[-3,1,-1]])
    print(k)