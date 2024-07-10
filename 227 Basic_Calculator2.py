import re
class Solution:
    def left_right(self, s):
        if s.isdigit():
            return int(s)

        operators = "+-*/"
        o = '/'
        ind = len(s)

        for i in range(len(s)):
            if s[i] in operators and operators.index(o) >= operators.index(s[i]):
                ind = i
                o = s[i]

        left = self.left_right(s[:ind])
        right = self.left_right(s[ind+1:])

        if o == "+":
            return left+right
        elif o == "-":
            return left-right
        elif o == "*":
            return left*right
        elif o == "/":
            return left//right

    def calculate(self, s: str) -> int:
        s = re.sub("\s+","",s)
        ans = self.left_right(s)
        return ans
        
s = Solution()
k = s.calculate("1+2*5/3+6/4*2")
print(k)