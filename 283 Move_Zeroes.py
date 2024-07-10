class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        l = 0 
        r = 0
        count_zero = 0

        for i in nums: 
            if i == 0:
                count_zero += 1
        if count_zero == len(nums):
            return nums
        while l != len(nums) or r != len(nums):
            while l < len(nums) and nums[l] == 0:
                l += 1
            while r < len(nums) and nums[r] != 0:
                r += 1
            if r >= len(nums)-count_zero or l >= len(nums):
                break
            if l>r:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
            if l<r:
                l += 1
        print(nums)

if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([1,0,1])