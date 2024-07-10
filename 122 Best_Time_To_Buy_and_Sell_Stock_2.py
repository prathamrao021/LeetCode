class Solution:
    def maxProfit(self, prices) -> int:
        dp = [0]*len(prices)
        dp[0] = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                dp[i] = dp[i-1]+(prices[i]-prices[i-1])
            else:
                dp[i] = dp[i-1]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    s.maxProfit([7,1,5,3,6,4])