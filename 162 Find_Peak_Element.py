class Solution:
    def findPeakElement(self, nums) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:

            return (0 if nums[0]> nums[1] else 1)
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = l+((r-l)//2)
            if mid == len(nums)-1 and nums[mid] > nums[mid-1]:
                return mid
            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            if mid+1 < len(nums) and mid-1>=0 and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                l = mid + 1
            elif mid-1 >= 0 and nums[mid] < nums[mid-1]:
                r = mid - 1

if __name__ == "__main__":
    s = Solution()
    k = s.findPeakElement([6,5,4,3,2,3,2])
    print(k)