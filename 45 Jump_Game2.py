class Solution:
    def calc_best(self, nums, ind, jumps):
        high_ind_val = 0
        ind_pass = 0
        for i in range(nums[ind]):
            if ind+i+1 < len(nums)-1 and nums[ind+i+1] + (i+1) > high_ind_val:
                high_ind_val = nums[ind+i+1] + i+1
                ind_pass = ind+i+1
            elif ind+i+1 == len(nums)-1:
                return jumps+1
        jumps=self.calc_best(nums, ind_pass, jumps+1)
        return jumps
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        jumps = 0
        jumps = self.calc_best(nums, 0, 0)
        return jumps

if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))
    # print(s.jump([2,3,0,1,4]))
    # print(s.jump([2,1]))