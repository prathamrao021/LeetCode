class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l)//2)
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] <= nums[r]:
                if nums[m-1] > nums[m]:
                    return nums[m]
                r = m -1
        # return nums[l]  
s = Solution()

k = s.findMin([4,5,6,7,0,1,2])
print(k)