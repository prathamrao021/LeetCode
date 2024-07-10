##DP question: will require time.

class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        ans = triangle[0][0]
        previous_ind = 0
        for inter_nums in range(len(triangle)):
            if previous_ind + 1 < len(triangle[inter_nums]):
                if triangle[inter_nums][previous_ind] < triangle[inter_nums][previous_ind+1]:
                    ans += triangle[inter_nums][previous_ind]
                    previous_ind = previous_ind
                elif triangle[inter_nums][previous_ind] > triangle[inter_nums][previous_ind+1]:
                    ans += triangle[inter_nums][previous_ind+1]
                    previous_ind = previous_ind+1
        return(ans)      

if __name__ == "__main__":
    s = Solution()
    triangle =[[-1],[2,3],[1,-1,-3]]
    k = s.minimumTotal(triangle)
    print(k)
        