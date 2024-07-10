class Solution:
    def isValid(self, s):
        brackets_stack = []
        pairs = ['{}','[]','()']
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "(" or s[i] == "[":
                brackets_stack.append(s[i])
            else:
                if (brackets_stack.pop()+s[i]) in pairs and len(brackets_stack) >= 1:
                    continue
                else:
                    return False
        if len(brackets_stack) != 0:
            return False
        return True
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("([)]"))