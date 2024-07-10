class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        remaining = 0
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            if numbers[i] > target and numbers[i] > 0:
                break
            if len(ans) > 0:
                ans.clear()
            remaining = target
            remaining -= numbers[i] 
            ans.append(i+1)
            for j in range(i+1,len(numbers)):
                if numbers[j] > remaining:
                    break
                if numbers[j] == remaining:
                    ans.append(j+1)
                    target -= numbers[i] 
                if len(ans) == 2:
                    return ans

if __name__ == "__main__":
    s = Solution()
    s.twoSum([-1,-1,1,1,1,1,1,1,1],-2)