class Solution:
    def search(self, nums, target):
        if len(nums) == 1 and target == nums[0]:
            return True
        elif len(nums) == 1 and target != nums[0]:
            return False
        
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                break
        if i == len(nums)-1:
            if nums[-1] < nums[-2]:
                nums = nums[i:]+nums[0:i]
            else:
                nums = nums
        else:
            nums = nums[i:]+nums[0:i]

        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2

            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid -1
            else:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.search([1,1], 2))