class Solution:
    def to_call_recursively(self, candidates, temp, sum, start,  final, target):
        if sum == target:
            final.append(temp)
            return
        elif sum < target:
            for index in range(start, len(candidates)):
                i = candidates[index]
                if sum + i > target:
                    return
                temp1 = list(temp)
                temp1.append(i)
                sum1 = sum + i
                self.to_call_recursively(candidates, temp1, sum1, index, final, target)
    
    def combinationSum(self, candidates, target):
        sum = 0
        final = []
        temp = []
        start = 0
        candidates.sort()
        self.to_call_recursively(candidates, temp, sum, start, final, target)
        return final

if __name__ == "__main__":
    s = Solution()
    k = s.combinationSum([2,3,8,4],6)
    print(k)