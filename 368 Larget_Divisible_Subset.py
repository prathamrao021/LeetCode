import collections
class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()
        dp = [1]*n

        max_size, max_i = 1, 0

        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_i = i

        result = []
        num = nums[max_i]

        for i in range(max_i,-1,-1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append(nums[i])
                num = nums[i]
                max_size -= 1
    
        return result


if __name__ =="__main__":
    s = Solution()
    print(s.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))