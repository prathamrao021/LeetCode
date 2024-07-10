class Solution:
    def houserobber(self, nums):
        if len(nums)== 1:
            return nums[0]
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
    def rob(self, nums) -> int:
        return max(self.houserobber(nums[1:]), self.houserobber(nums[:-1]))

if __name__ == "__main__":
    s = Solution()
    k = s.rob([1,2,1,1])
    print(k)