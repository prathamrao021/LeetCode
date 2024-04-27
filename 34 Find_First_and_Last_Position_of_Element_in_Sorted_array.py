
class Solution():
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
    
        while low <= high:
            if nums[low] < target:
                low += 1

            if nums[high] > target:
                high -= 1

            if nums[high] == target and  nums[low] == target:
                break
        
        if low > high:
            return([-1,-1])
        else:
            return([low,high])

s = Solution()
j = s.searchRange([5,7,8,9,9,12,12,12,15], 12)
print(j)      