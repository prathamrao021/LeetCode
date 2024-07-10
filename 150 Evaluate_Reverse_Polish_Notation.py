import math
class Solution:
    def evalRPN(self, tokens):
        ans_stack = [tokens[0]]
        i = 1
        operators = set(["*","+","/","-"])
        ans = [tokens[0]]
        while i != len(tokens) :
            if tokens[i] in operators:
                a = int(ans_stack.pop())
                b = int(ans_stack.pop())
                if tokens[i] == "*":
                    ans = a*b
                if tokens[i] == "-":
                    ans = b-a
                if tokens[i] == "/":
                    if (a < 0 and b > 0) or (a > 0 and b < 0): 
                        ans = math.ceil(b/a)
                    else:
                        ans = b//a
                if tokens[i] == "+":
                    ans = a+b
                ans_stack.append(str(ans))
            else:
                ans_stack.append(tokens[i])
            i += 1
        return(ans)

if __name__ == "__main__":
    s = Solution()
    k = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(k)