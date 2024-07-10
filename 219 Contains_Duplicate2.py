import collections
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        ans = 0
        uni = collections.defaultdict(list)
        # first_app = 0
        for i in range(len(nums)):
            if uni.get(nums[i]) != None and len(uni.get(nums[i])) >= 1:
                for j in uni[nums[i]]:
                    ans = abs(j-i)
                    if ans <= k:
                        return True
            uni[nums[i]].append(i)
        return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))