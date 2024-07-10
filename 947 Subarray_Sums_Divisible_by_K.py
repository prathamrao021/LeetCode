# class Solution:
#     def calculate(self, nums, k, temp_sum, ind):
#         if temp_sum % k == 0:
#             self.count += 1

#         if ind != len(nums)-1:
#             self.calculate(nums, k, temp_sum+nums[ind+1], ind+1)
#         return
        
#     def subarraysDivByK(self, nums, k: int) -> int:
#         temp_sum = 0
#         self.count = 0
#         ind = 0
#         for ind in range(len(nums)):
#             self.calculate(nums, k, temp_sum+nums[ind], ind)
#         return self.count
    
class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        count = 0
        remainder_freq = {0:1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            key = prefix_sum % k
            if key in remainder_freq:
                count += remainder_freq[key]
                remainder_freq[key] += 1
            else:
                remainder_freq[key] = 1
        return count

if __name__ == '__main__':
    s = Solution()
    k = s.subarraysDivByK([4,5,0,-2,-3,1],5)
    print(k)
        
