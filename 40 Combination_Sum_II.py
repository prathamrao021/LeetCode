class Solution:
    def get_combination(self, candidates, target, curr_sum, idx, temp_list ,final_list):
        if target == curr_sum and temp_list not in final_list:
            final_list.append(temp_list.copy())
            return

        elif target < curr_sum: return
        else:
            for i in range(idx, len(candidates)):
                if i>=1 and candidates[i] == candidates[i-1] and len(temp_list) == 0:
                    continue
                temp_list.append(candidates[i])
                curr_sum += candidates[i]
                self.get_combination(candidates, target, curr_sum, i+1, temp_list ,final_list)
                temp_list.pop()
                curr_sum -= candidates[i]
            
    def combinationSum2(self, candidates, target):
        final_list = []
        candidates.sort()
        self.get_combination(candidates, target, 0, 0, [],final_list)
        return final_list
    
# another way of adding in the list is <list>+[element]


if __name__ == "__main__":
    s = Solution()
    candidates = [10,1,2,7,6,1,5] #[1,1,2,5,6,7,10]
    target = 8
    k = s.combinationSum2(candidates,target)
    print(k)