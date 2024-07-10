class Solution:                    
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s) #8
        dp = [False]*(n+1)
        dp[n] = True

        for i in range(n-1,-1,-1):
            #use i-1 in "s" and i in "dp"
            for w in wordDict:
                if s[i:].startswith(w):
                    if dp[i] == True:
                        break
                    dp[i] = dp[i+len(w)]
        print(dp)
        return dp[0]  
        
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("abcd",["a","abc","b","cd"]))
        