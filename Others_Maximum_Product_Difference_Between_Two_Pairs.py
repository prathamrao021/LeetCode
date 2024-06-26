class Solution():
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = float('inf')
        min1_ind = 0
        min2 = float('inf')
        min2_ind = 0
        max1_ind = 0
        max1 = 0
        max2_ind = 0
        max2 = 0

        for i in range(len(nums)):
            if nums[i]>max1:
                max1 = nums[i]
                max1_ind = i    
        nums[max1_ind] = 0

        for i in range(len(nums)):
            if nums[i]>max2:
                max2 = nums[i]
                max2_ind = i
        nums[max2_ind] = 0

        for i in range(len(nums)):
            if nums[i] < min1 and nums[i] != 0:
                min1 = nums[i]
                min1_ind = i
        nums[min1_ind] = 0
    
        for i in range(len(nums)):
            if nums[i] < min2 and nums[i] != 0:
                min2 = nums[i]
                min2_ind = i
        nums[min2_ind] = 0

        return((max1*max2)-(min1*min2))

s = Solution()
k = s.maxProductDifference([4,2,5,9,7,4,9])
print(k)