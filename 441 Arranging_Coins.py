import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(n+1):
            if (i*(i+1))//2 > n:
                return i-1

s = Solution()
print(s.arrangeCoins(5))