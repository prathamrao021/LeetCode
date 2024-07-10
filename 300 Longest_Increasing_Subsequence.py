class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

s = Solution()
k = s.lengthOfLIS([4,10,4,3,8,9])
print(k)