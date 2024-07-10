class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [[float("inf") for _ in range(amount+1)] for _ in range(len(coins)+1)]
        
        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                if j == 0:
                    dp[i][j] = 0
                    continue
                elif coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                elif coins[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
        return(dp[-1][-1] if dp[-1][-1] != float('inf') else -1)

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([2],3))
        