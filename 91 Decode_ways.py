# class Solution:
#     def calculate(self, s, k, ans, temp_ans):
#         if k >= len(s):
#             ans.append(temp_ans)
#             return
#         # print(s[k:k+2])
#         if int(s[k]) != 0:
#             self.calculate(s,k+1,ans,temp_ans+[s[k]])
#             if int(s[k:k+2]) <= 26 and k+2 <= len(s):
#                 self.calculate(s,k+2,ans,temp_ans+[s[k:k+2]])
#         return

#     def numDecodings(self, s):
#         temp_ans = []
#         ans = []
#         #65  to 90
#         self.calculate(s, 0, ans, temp_ans)
#         return len(ans)

class Solution:
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,len(s)+1):
            o_num = int(s[i-1])
            t_num = int(s[i-2:i])

            if o_num != 0:
                dp[i] = dp[i-1]
            if 10 <= t_num <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    k = s.numDecodings("06")
    print(k)