class Solution:
    def removeDuplicates(self, nums):
        hashmap = {}
        ans = len(nums)
        deleted = 0
        i = 0
        while i < len(nums):   
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
                i += 1
            elif hashmap[nums[i]] == 1:
                hashmap[nums[i]] = 2
                i += 1
            else:
                print(i)
                ans -= 1
                nums.remove(nums[i])
                deleted += 1
        for i in range(deleted):
            nums.append(0)        
        return (ans)
        
if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([1,1,1,2,2,3])