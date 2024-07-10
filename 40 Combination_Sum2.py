import collections
class Solution:
    def get_combination(self, candidates, target, idx, temp_list):
        if target == 0 and temp_list not in self.final_list:
            self.final_list.append(temp_list)
        else:
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if target-candidates[i] >= 0:
                    self.get_combination(candidates, target-candidates[i], i+1, temp_list+[candidates[i]])

        
            
    def combinationSum2(self, candidates, target):
        self.final_list = []
        candidates.sort()

        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            else:  
                self.get_combination(candidates, target-candidates[i], i+1, [candidates[i]])
        return self.final_list

if __name__ == "__main__":
    s = Solution()
    k = s.combinationSum2([2,5,2,1,2], 5)
    print(k)
