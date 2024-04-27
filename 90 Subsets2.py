class Solution:
    def calculate(self, nums, int_len, ans, temp_ans, k):
        if len(temp_ans) == int_len:
            if temp_ans not in ans:
                ans.append(temp_ans)
            return
        for i in range(k,len(nums)):
            self.calculate(nums, int_len, ans, temp_ans+[nums[i]], i+1)
        return
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        temp_ans = []
        for i in range(len(nums)+1):
            self.calculate(nums, i, ans, temp_ans, 0)
        return ans

if __name__ == "__main__":
    s = Solution()
    k = s.subsetsWithDup([1,2,2])
    print(k)
        