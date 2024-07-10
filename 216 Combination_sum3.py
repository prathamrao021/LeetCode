class Solution:
    def calculate(self, k, n, temp_sum, temp_curr, temp_list):
        if temp_sum == n and len(temp_list) == k:
            self.final.append(temp_list.copy())
            return
        elif temp_sum < n:
            if len(temp_list) >= k:
                return
            # elif temp_curr == n:
            #     return 
            elif len(temp_list) < k:
                for i in range(temp_curr+1, min(n,10)):
                    self.calculate(k, n, temp_sum+i, i, temp_list+[i])
        else:
            return
    def combinationSum3(self, k: int, n: int):
        self.final = []
        for i in range(1, min(n,10)):
            self.calculate(k, n, i, i, [i])
        return(self.final)

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(2,18))