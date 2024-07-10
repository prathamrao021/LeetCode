import collections
# class Solution:
#     def hasGroupsSizeX(self, deck) -> bool:
#         def common_factor(num1,num2):
#             for i in range(2,min(num1,num2)+1):
#                 if num1%i == 0 and num2%i == 0:
#                     return i
#             return 0
#         freq_table  = collections.Counter(deck)
#         same = float('inf')
#         for key,val in freq_table.items():
#             if val == 1:
#                 return False
#             if same == float('inf'):
#                 same = val
#             if same != val:
#                 same = common_factor(same,val)
#                 if same < 2:
#                     return False
#         return True

import math
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        def common_factor(num1,num2):
            for i in range(2,min(num1,num2)+1):
                if num1%i == 0 and num2%i == 0:
                    return i
            return 1
        f=collections.Counter(deck)
        u=list(f.values())
        g=u[0]
        
        for j in range(1,len(u)):
            g=common_factor(g,u[j])
        return g!=1
    

if __name__ =="__main__":
    s = Solution()
    print(s.hasGroupsSizeX([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]))