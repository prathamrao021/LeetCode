class Solution:
    def maxProduct(self, nums) -> int:
        max_pro = nums[0]
        currmax_pro = nums[0]
        currmin_pro = nums[0]
        for i in range(1,len(nums)):
        #     if curr_pro > curr_pro*nums[i]:
        #         curr_pro = 1
        #     else:
        #         curr_pro *= nums[i]
            
        #     if curr_pro > max_pro:
        #         max_pro = curr_pro
        # print(max_pro)
        # return max_pro
            s = [nums[i], currmax_pro*nums[i], currmin_pro*nums[i]]
            currmax_pro = max(s)
            currmin_pro = min(s)
            max_pro = max(max_pro, currmax_pro)
        
        return(max_pro)

    
if __name__ == "__main__":
    s = Solution()
    s.maxProduct([-2,3,-4])