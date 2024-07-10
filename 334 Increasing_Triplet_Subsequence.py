class Solution:
    def increasingTriplet(self, nums) -> bool:
        # dp = [1]*len(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] > nums[i]:
        #             dp[j] = max(dp[j],dp[i]+1)
        # return True if max(dp) >= 3 else False

        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # smallest so far
            elif n <= second:
                second = n  # second smallest
            else:
                return True  # found a triplet
        
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([20,100,10,12,5,13]))