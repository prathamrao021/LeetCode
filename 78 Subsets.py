class Solution:
    def calc_subset(self, nums, ans, ans_temp, temp):
        ans.append(ans_temp)
        for i in range(temp, len(nums)):
            if nums[i] not in ans_temp:
                ans = self.calc_subset(nums,ans,ans_temp + [nums[i]], i)
        return ans
            
    def subsets(self, nums):
        ans = []
        ans_temp = []
        if len(nums) == 1:
            ans.append([])
            ans.append(nums)
            return ans
        else:
            self.calc_subset(nums, ans, [], 0)
            return ans

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))