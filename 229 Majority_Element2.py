class Solution:
    def majorityElement(self, nums):

        count1, count2 = 0,0

        can1, can2 = 0,0

        for i in range(len(nums)):
            if count1 == 0 and nums[i] != can1 and nums[i] != can2:
                count1 = 1
                can1 = nums[i]
            elif count2 == 0 and nums[i] != can2 and nums[i] != can1:
                count2 = 1
                can2 = nums[i]
            elif nums[i] == can1:
                count1 += 1
            elif nums[i] == can2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
            
        threshhold = len(nums)//3

        count1, count2 = 0, 0
        ans = []
        for i in range(len(nums)):
            if nums[i] == can1:
                count1 += 1
            elif nums[i] == can2:
                count2 += 1
            
        if count1 > threshhold:
            ans.append(can1)
        if count2 > threshhold:
            ans.append(can2)
    
        return ans

if __name__ == "__main__":
    s = Solution()
    k = s.majorityElement([1,1,2,3,4,1,1,5,6,7,1,1,8,9,10,1,11,12,13,14])
    print(k)