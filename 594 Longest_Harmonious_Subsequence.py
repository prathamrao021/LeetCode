class Solution:
    def findLHS(self, nums) -> int:
        dp  = [0 for i in range(len(nums))]
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(i):
                if abs(nums[i]-nums[j]) <= 1:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return 0 if dp[-1] == 0 else dp[-1]+1
s = Solution()
s.findLHS([1,3,2,2,5,2,3,7])