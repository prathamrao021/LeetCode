class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        var = (n*(n+1))/2 - sum(nums)
        return(var)

if __name__ == "__main__":
    s = Solution()
    k = s.missingNumber([3,0,1])
    print(k)