class Solution:
    def smallestRangeI(self, nums, k: int) -> int:
        max_num = nums[0]
        min_num = nums[0]
        for i in range(1,len(nums)):
            max_num = max(max_num,nums[i])
            min_num = min(min_num,nums[i])
        x = (max_num-k)-(min_num+k) 
        return x if x > 0 else 0

if __name__ == "__main__":
    s = Solution()
    print(s.smallestRangeI([3,1,10],4))