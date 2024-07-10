class Solution:
    def summaryRanges(self, nums):
        start = nums[0]
        end = nums[0]
        inter_str = ''
        final_ans = []
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i+1] == nums[i] + 1:
                end = nums[i+1]
            else:
                if end-start >= 1:
                    inter_str = str(start)+"->"+str(end)
                else:
                    inter_str = str(start)
                final_ans.append(inter_str)
                inter_str = ''
                if i+1 < len(nums):
                    start = nums[i+1]
                    end = nums[i+1]
        return final_ans

if __name__ == "__main__":
    s = Solution()
    k = s.summaryRanges([0,1,2,4,5,7])
    print(k)