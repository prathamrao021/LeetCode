class Solution:
    # def calculate(self, target, nums, ind, temp_arr):
    def minSubArrayLen(self, target: int, nums) -> int:
        
        i,j = 0,1
        add = nums[0]+nums[1]
        mini_len = float('inf')
        
        while j < len(nums):
            while i < len(nums) and i <= j:
                if add == target:
                    mini_len = min(mini_len, j-i+1)
                    add -= nums[i]
                    i += 1
                    j += 1
                    if j == len(nums):
                        break
                    add += nums[j]
                elif add > target:
                    add -= nums[i]
                    i += 1
                elif add < target:
                    j += 1
                    if j == len(nums):
                        break
                    add += nums[j]
            if i > j:
                j = i+1
        if j >= len(nums) and mini_len == float('inf'):
            return 0
        return(mini_len)

if __name__ == "__main__":
    s = Solution()
    k = s.minSubArrayLen(11,[1,1,1,1,1,1,1,1,1,1])
    print(k)