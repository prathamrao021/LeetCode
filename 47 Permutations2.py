## had to see the solution
class Solution:
    def recursive(self, nums, temp_ans, ans, count_dict):
        if len(temp_ans) == len(nums):
            ans.append(temp_ans)
            return
        else:
            for i in count_dict:
                if count_dict[i]:
                    count_dict[i] -= 1
                    self.recursive(nums, temp_ans+[i], ans, count_dict)
                    count_dict[i] += 1
        return ans
    
    def permuteUnique(self, nums):
        count_dict = {}
        # counter = Counter(nums)
        ans = []
        for i in range(len(nums)):
            if nums[i] not in count_dict.keys():
                count_dict[nums[i]] = 1
            else:
                count_dict[nums[i]] += 1
        ans = self.recursive(nums, [], [], count_dict)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1,1,2]))