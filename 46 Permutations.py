class Solution:
    def recursion(self, nums, temp_ans, ans):
        if len(temp_ans) == len(nums):
            ans.append(temp_ans)
        for i in range(len(nums)):
            if nums[i] not in temp_ans:
                self.recursion(nums, temp_ans+[nums[i]], ans)
        return ans
    
    def permute(self, nums):
        ans = []
        ans = self.recursion(nums, [], [])
        return ans
        
if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))