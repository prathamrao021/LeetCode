class Solution:
    def calculate(self, expression):
        if expression.isdigit():
            return [int(expression)]
        res= []
        for exp in range(len(expression)):
            if expression[exp] in "*-+":
                left = self.calculate(expression[:exp])
                right = self.calculate(expression[exp+1:])
                for l in left:
                    for r in right:
                        if expression[exp] == "+":
                            res.append(l+r)
                        elif expression[exp] == "-":
                            res.append(l-r)
                        elif expression[exp] == "*":
                            res.append(l*r)
        return res
    def diffWaysToCompute(self, expression: str):
        result = [] 

        result = self.calculate(expression)
        return result

s = Solution()
print(s.diffWaysToCompute("2*3-4*5"))