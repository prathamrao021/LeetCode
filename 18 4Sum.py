class Solution:
    def calculate(self, nums, ind, temp, target_left):
        n = len(nums)
        if len(temp) == 4 and target_left == 0 and tuple(temp) not in self.ans:
            self.ans.add(tuple(temp.copy()))
            return
        if len(temp) == 4:
            return
        for i in range(ind+1,n):
            self.calculate(nums, i, temp+[nums[i]], target_left-nums[i])
        return 

        
    def fourSum(self, nums, target: int):
        n = len(nums)
        # num_set = set(nums)
        self.ans = set()
        temp = []
        for i in range(n):
              self.calculate(nums, i, temp+[nums[i]], target-nums[i])
        return list(self.ans)

if __name__ == "__main__":
    s = Solution()
    k = s.fourSum([-5,5,4,-3,0,0,4,-2],4)
    print(k)