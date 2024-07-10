# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s1)+len(s2) < len(s3):
#             return False
#         #Handle extreme cases.
#         i = 0 #s1
#         j = 0 #s2
#         k = 0 #s3
#         turn = True #True for s1 and False for s2
#         while True:
#             if turn:
#                 if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
#                     turn = True
#                     i += 1
#                     k += 1
#                 elif j < len(s2) and k < len(s3) and s2[j] == s3[k]:
#                     turn = False
#                     j += 1
#                     k += 1
#                 elif j == len(s2) and i == len(s1):
#                     return True
#                 else:
#                     return False
#             else:
#                 if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
#                     turn = False
#                     j += 1
#                     k += 1
#                 elif i < len(s1) and k < len(s3) and s1[i] == s3[k]:
#                     turn = True
#                     i += 1
#                     k += 1
#                 elif j == len(s2) and i == len(s1):
#                     return True
#                 else:
#                     return False

class Solution:
    def calculate(self, s1, s2, s3, s1_var, s2_var, s3_var, ans):
        if s1_var < len(s1) and s2_var < len(s2) and s3_var < len(s3):
            if s1[s1_var] == s3[s3_var] and s2[s2_var] != s3[s3_var]:
                ans = self.calculate(s1, s2, s3, s1_var+1, s2_var, s3_var+1, ans)
                return ans
            elif s1[s1_var] != s3[s3_var] and s2[s2_var] == s3[s3_var]:
                ans = self.calculate(s1, s2, s3, s1_var, s2_var+1, s3_var+1, ans)
                return ans
            elif s1[s1_var] == s3[s3_var] and s2[s2_var] == s3[s3_var]:
                ans = self.calculate(s1, s2, s3, s1_var, s2_var+1, s3_var+1, ans) or self.calculate(s1, s2, s3, s1_var+1, s2_var, s3_var+1, ans)
                return ans
            else:
                return False
        elif s2_var == len(s2) and s1_var != len(s1) and s3_var != len(s3):
            if s1[s1_var] == s3[s3_var]:
                ans = self.calculate(s1, s2, s3, s1_var+1, s2_var, s3_var+1, ans)
                return ans
            else:
                return False
        elif s2_var != len(s2) and s1_var == len(s1) and s3_var != len(s3):
            if s2[s2_var] == s3[s3_var]:
                ans = self.calculate(s1, s2, s3, s1_var, s2_var+1, s3_var+1, ans)
                return ans
            else:
                return False
        elif s2_var == len(s2) and s1_var == len(s1) and s3_var == len(s3):
            return True
        else:
            return False
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) < len(s3):
            return False
        return self.calculate(s1,s2,s3,0,0,0, True)
        

 
if __name__ == '__main__':
    s = Solution()
    print(s.isInterleave("a","b","a"))