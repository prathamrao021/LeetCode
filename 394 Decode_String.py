class Solution:
    # def decode(self, s):
    #     #can do by stack without recursion
    #     if self.index >= len(s):
    #         return ""
    #     ans = ''
    #     n = 0
    #     while self.index < len(s) and s[self.index] != ']':
    #         if s[self.index].isdigit():
    #             # n = int(s[self.index])
    #             # self.index+=2
    #             # ans += ((self.decode(s))*n)
    #             # if self.index >= len(s):
    #             #     return ""
    #             n = n*10 + int(s[self.index])
    #         elif s[self.index] == "[":
    #             self.index += len(str(self.index))
    #             ans += ((self.decode(s))*n)
    #             n=0
    #             if self.index >= len(s):
    #                 return ""
    #         else:
    #             ans = ans+s[self.index]
    #         self.index+=1
    #     return ans

    # def decodeString(self, s: str) -> str:
    #     res = ''
    #     self.index = 0
    #     res = self.decode(s)
    #     return res

    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for i in range(len(s)):
            if s[i].isdigit():
                curNum = curNum*10 +int(s[i])
            elif s[i] == "[":
                stack.append(curNum)
                stack.append(curString)
                curNum = 0
                curString = ''
            elif s[i] == "]":
               x = stack.pop()
               y = stack.pop()
               curString = x + y*curString
            else:
                curString = curString+s[i]
        return curString


if __name__ == "__main__":
    s = Solution()
    # print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
    print(s.decodeString("3[a2[c]]"))