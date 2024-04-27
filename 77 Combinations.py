class Solution:
    def calculate(self, n, k, ans, ans_temp, k_temp):
        if len(ans_temp) == k:
            ans.append(ans_temp)
            return ans
        for i in range(k_temp+1, n+1):
            ans = self.calculate(n, k, ans, ans_temp+[i], i)
        return ans
    def combine(self, n, k):
        ans = []
        ans_temp = []
        if k == n:
            for i in range(1,k+1):
                ans_temp.append(i)
            ans.append(ans_temp)
        else:
            ans = self.calculate(n, k, ans, ans_temp, 0)
        return ans

s = Solution()
print(s.combine(4,3))