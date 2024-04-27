class Solution:
    def calc(self, x,n,temp_ans,final_ans):
        if n == 0:
            final_ans = temp_ans
            return final_ans
        else:
            final_ans = self.calc(x,n-1,temp_ans*x, final_ans)
        return final_ans
    def pow(self,x,n):
        final_ans = 1
        temp_ans = 1
        
        final_ans = self.calc(x,n, temp_ans,final_ans)
        return final_ans

if __name__ == "__main__":
    s = Solution()
    k = s.pow(2,10)
    print(k)