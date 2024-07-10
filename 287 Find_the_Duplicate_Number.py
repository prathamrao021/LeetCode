class Solution:
    def findDuplicate(self, nums) -> int:
        i = 0
        n = len(nums)
        while i < len(nums):
            m = nums[i] % n
            if nums[m-1] == nums[i]:
                i += 1
            else:
                nums[i],nums[m-1] = nums[m-1],nums[i]
        return nums[-1]


s = Solution()
print(s.findDuplicate([1,3,4,2,2]))