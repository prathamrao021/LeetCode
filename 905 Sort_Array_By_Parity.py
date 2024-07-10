class Solution:
    def sortArrayByParity(self, nums):
        low = 0
        high = len(nums)-1

        while low < high:
            while low < high and nums[low]%2 == 0:
                low += 1
            while high > low and nums[high]%2 == 1:
                high -= 1
            nums[low],nums[high] = nums[high],nums[low]
            low += 1
            high -= 1
        return nums
    
if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParity([0,2]))