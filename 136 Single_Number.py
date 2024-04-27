class Solution:
    def singleNumber(self, nums):
        xor_ans = 0
        for i in range(len(nums)):
            xor_ans = xor_ans ^ nums[i]
        return xor_ans
    
    
if __name__ == "__main__":
    s = Solution()
    k = s.singleNumber([1,1,3,4,3])
    print(k)