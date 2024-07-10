class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        int_ans = n
        while int_ans >= 10:
            int_ans = 0
            while num != 0:
                digit = num%10
                int_ans += (digit**2)
                num = num//10
                print(int_ans)
            num = int_ans
            if int_ans == 1 or int_ans == 7:
                return True
        if int_ans == 1:
            return True
        else:
            if n == 7 or n == 1:
                return True
            return False
    
if __name__ == '__main__':
    n = 1111111
    s = Solution()
    s.isHappy(n)
