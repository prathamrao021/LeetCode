
class Solution:
    def remove_max(self, list_in_list, nums):
        j = 0 #bit
        i = 0 #ind
        max_ind = 0
        max_val = 0
        while j < max([len(i) for i in list_in_list]):
            max_val = 0
            for i in range(len(list_in_list)):
                if j < len(list_in_list[i]):
                    if list_in_list[i][j] > max_val:
                        max_ind = i
                        max_val = list_in_list[i][j]
                else:
                    if list_in_list[i][-1] > max_val:
                        max_ind = i
                        max_val = list_in_list[i][-1]
            j += 1
        del list_in_list[max_ind]
        return (list_in_list,nums[max_ind])
    

    def largestNumber(self, nums) -> str:
        list_in_list = []
        for i in range(len(nums)):
            if len(str(nums[i])) == 1:
                list_in_list.append([nums[i]])
            else:
                temp = []
                for j in range(len(str(nums[i]))):
                    temp.append(int(str(nums[i])[j]))
                list_in_list.append(temp)

        ans = ""
        while list_in_list:
            list_in_list,max_val = self.remove_max(list_in_list, nums)
            nums.remove(max_val)
            ans += str(max_val)
        return(ans)
if __name__ == "__main__":
    s = Solution()
    s.largestNumber([3,30])