class Solution:
    def canJump(self, nums):
        arr = [0]*len(nums)
        arr[0] = nums[0]
        if len(nums) == 1:
            return True
        if arr[0] == 0:
            return False
        flag = True
        # while i != len(nums)-1:
        for i in range(1,len(nums)-1):
            arr[i] =  max(arr[i-1], i+nums[i])
            if arr[i] == i:
                return False
        if arr[-2] >= len(nums)-1:
            return True
        else:
            return False
if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4])) # True
    print(s.canJump([3,2,1,0,4])) # False
    print(s.canJump([0])) # True
    print(s.canJump([2,0,0])) # True
    print(s.canJump([2,0])) # True
    print(s.canJump([0,2,3])) # False
    print(s.canJump([2,0,2,0,1])) # True