class Solution:
    def calculate(self, target, nums, ind, temp_arr):
        if target <= 0:
            self.min_len = min(self.min_len, len(temp_arr))
            # temp_arr = []
            return

        elif target > 0:
            for i in range(ind, len(nums)):
                self.calculate(target-nums[i],nums,i+1,temp_arr+[nums[i]])
            return 
    def minSubArrayLen(self, target: int, nums) -> int:
        self.min_len = float('inf')
        for i in nums:
            if i == target:
                return 1
        temp_arr = []
        for i in range(len(nums)):
            self.calculate(target-nums[i],nums,i+1,temp_arr+[nums[i]])
        if self.min_len == float('inf'):
            return 0
        return (self.min_len)
    
if __name__ == "__main__":
    s = Solution()
    k = s.minSubArrayLen(11,[1,1,1,1,1,1,1,1,1,1])
    print(k)