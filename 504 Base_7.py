class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:return "0"
        neg = False
        if num < 0:
            neg = True
            num = -1*num
        ans = ''
        while num != 0:
            ans = str(num%7) + ans
            num = num//7
        if neg:
            ans = '-'+ans
        return ans

s = Solution()
print(s.convertToBase7(100))