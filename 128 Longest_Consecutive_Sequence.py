# class Solution:
    # to get entire array of sequence
    # def plus_minus_one(self, curr_num, nums_set, seq_arr,final_ans):
    #     final_ans = seq_arr.copy() if(len(seq_arr)>len(final_ans)) else final_ans
    #     if curr_num+1 in nums_set and curr_num+1 not in seq_arr:
    #         seq_arr.add(curr_num+1)
    #         final_ans = self.plus_minus_one(curr_num+1,nums_set,seq_arr,final_ans)
    #         seq_arr.remove(curr_num+1)
    #     if curr_num-1 in nums_set and curr_num-1 not in seq_arr:
    #         seq_arr.add(curr_num-1)
    #         final_ans = self.plus_minus_one(curr_num-1,nums_set,seq_arr,final_ans)
    #         seq_arr.remove(curr_num-1)
    #     return final_ans
    # def longestConsecutive(self, nums) -> int:
    #     final_ans = set()
    #     ans = set()
    #     nums_set = set(nums)
    #     for i in range(len(nums)):
    #         if nums[i] not in final_ans:
    #             ans.add(nums[i])
    #             final_ans = self.plus_minus_one(nums[i],nums_set,ans,final_ans)
    #             ans.remove(nums[i])
                
    #     return len(final_ans)
    



    #to get count
    # def plus_minus_one(self, curr_num, nums_set, seq_arr,final_ans):
    #     final_ans = len(seq_arr) if(len(seq_arr)>(final_ans)) else (final_ans)
    #     if curr_num+1 in nums_set and curr_num+1 not in seq_arr:
    #         seq_arr.add(curr_num+1)
    #         final_ans = self.plus_minus_one(curr_num+1,nums_set,seq_arr,final_ans)
    #         seq_arr.remove(curr_num+1)
    #     if curr_num-1 in nums_set and curr_num-1 not in seq_arr:
    #         seq_arr.add(curr_num-1)
    #         final_ans = self.plus_minus_one(curr_num-1,nums_set,seq_arr,final_ans)
    #         seq_arr.remove(curr_num-1)
    #     return final_ans
    # def longestConsecutive(self, nums) -> int:
    #     final_ans = 0
    #     ans = set()
    #     nums_set = set(nums)
    #     for i in range(len(nums)):
    #         if nums[i] not in ans:
    #             ans.add(nums[i])
    #             final_ans = self.plus_minus_one(nums[i],nums_set,ans,final_ans)
    #             ans.remove(nums[i])
                
    #     return (final_ans)
                

##Actual Ans:
class Solution:    
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        final_ans = 1
        ans = 1
        nums = set(nums)
        for x in nums:
            if x-1 not in nums:
                ans = 1
                y = x+1
                while y in nums:
                    ans += 1
                    y += 1
                final_ans = max(ans,final_ans)
        return final_ans

if __name__ == "__main__":
    s = Solution()
    nums = [100,4,200,1,3,2]
    k = s.longestConsecutive(nums)
    print(k)