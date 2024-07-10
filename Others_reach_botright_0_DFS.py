class Solution:
    def dfs(self,matrix,distance):
        pass
    def reach_bot_right_zero(self,matrix):
        pass
if __name__ == "__main__":
    matrix = [[0,0,0],[1,1,0],[1,1,0]]
    # matrix = [[0,0,0,0],[1,0,1,1],[1,0,0,0],[1,1,1,0]]
    # matrix = [[0,1,1,1],[0,0,0,0],[1,0,1,0],[1,1,1,0]]
    s = Solution()
    k, p = s.reach_bot_right_zero(matrix)
    print(k,p)
