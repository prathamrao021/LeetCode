class Solution:
    def findMaxAverage(self, nums, k) -> float:
        max_sum = sum(nums[:k])
        curr_sum = sum(nums[:k])
        for i in range(k,len(nums)):

            curr_sum += nums[i] - nums[i - k]
            max_sum = max(curr_sum, max_sum)
        # print(arr)
        return (max_sum/k)

    
if __name__ == "__main__":
    s = Solution()
    s.findMaxAverage([1,12,-5,-6,50,3], 4)
        