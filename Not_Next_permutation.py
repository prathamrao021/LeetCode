class Solution:
    def next_per(self, nums):
        no_change = False
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] >= nums[i]:
                no_change = True
                pass
            elif nums[i-1] < nums[i]:
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
                no_change = False
                break
            
        if no_change == False:
            new_nums = list(nums[i] for i in range(i,len(nums)))
            nums = nums[0:i] + sorted(new_nums)
        if no_change == True:
            nums = sorted(nums)    
        return nums

s = Solution()
per = [3,2,1]
j = s.next_per(per)
print(j)