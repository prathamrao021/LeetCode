class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if i == 0:
                    dp[i][j] = 0
                    continue
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif j >= coins[i-1]:
                    dp[i][j] = dp[i][j-coins[i-1]]+dp[i-1][j]
        
        return dp[len(coins)][amount]