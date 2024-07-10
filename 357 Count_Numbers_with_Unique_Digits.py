class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0]*n 
        dp[0] = 10
        for i in range(1,n):
            ans = 1
            for j in range(i+1):
                if j == 0:
                    ans *= 9
                else:
                    ans *= (10-j)
            dp[i] = dp[i-1]+ans
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.countNumbersWithUniqueDigits(3))