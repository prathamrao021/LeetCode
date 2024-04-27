class Solution:
    def minDistance(self, word1, word2):
        l1 = len(word1)+1
        l2 = len(word2)+1
        dp = []
        for i in range(l1):
            temp = []
            for j in range(l2):
                temp.append(0)
            dp.append(temp)
        
        for i in range(l1):
            for j in range(l2):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
        return(dp[-1][-1])

if __name__ == "__main__":
    s = Solution()
    print(s.minDistance('horse','ros'))