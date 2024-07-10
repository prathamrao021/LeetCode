import collections
class Solution:
    def findShortestSubArray(self, nums) -> int:
        freq_table = collections.Counter(nums)
        max_val = []
        max_freq = 0
        for key,val in freq_table.items():
            if max_freq < val:
                max_freq = val
                max_val.clear()
                max_val.append(key)
            elif max_freq == val:
                max_val.append(key)

        if max_freq == 1: return 1
        
        min_diff = float('inf')
        
        for i in max_val:
            start = float('inf')
            finish = float('inf')
            for j in range(len(nums)):
                print(len(nums)-1-j,j)
                if start == float('inf') and nums[j] == i:
                    start = j
                if finish == float('inf') and nums[len(nums)-1-j] == i:
                    finish = len(nums)-1-j
            min_diff = min(min_diff,finish-start)    
        return min_diff+1

s = Solution()
print(s.findShortestSubArray([1,2,2,3,1]))