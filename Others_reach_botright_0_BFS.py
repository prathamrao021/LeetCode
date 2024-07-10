class Solution:
    def reach_bot_right_zero(self,matrix):
        num_of_zeros = 1
        distance = [[float('inf')]*(len(matrix[0])) for _ in range(len(matrix))]
        zero_queue = [[0,0]]
        matrix[0][0] = 1
        distance[0][0] = 1
        while len(zero_queue) != 0:
            curr_pos = zero_queue.pop(0)
            for i in range(min(curr_pos[0]+1, len(matrix[0])-1),curr_pos[0]-1,-1):
                for j in range(min(curr_pos[1]+1, len(matrix[0])-1), curr_pos[1]-1,-1):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 1
                        distance[i][j] = distance[curr_pos[0]][curr_pos[1]]+1
                        zero_queue.append([i,j])
                        if i == len(matrix)-1 and j == len(matrix[0])-1:
                            return True, distance[len(matrix[0])-1][len(matrix)-1]
        return False, distance[len(matrix[0])-1][len(matrix)-1]
if __name__ == "__main__":
    matrix = [[0,0,0],[1,1,0],[1,1,0]]
    # matrix = [[0,0,0,0],[1,0,1,1],[1,0,0,0],[1,1,1,0]]
    # matrix = [[0,1,1,1],[0,0,0,0],[1,0,1,0],[1,1,1,0]]
    s = Solution()
    k, p = s.reach_bot_right_zero(matrix)
    print(k,p)
