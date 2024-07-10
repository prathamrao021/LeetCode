class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        remainder_cache = {0:-1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %=k
            if remainder not in remainder_cache:
                remainder_cache[remainder] = i
            elif i - remainder_cache[remainder] >=2:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.checkSubarraySum([23,2,6,4,6], 6))