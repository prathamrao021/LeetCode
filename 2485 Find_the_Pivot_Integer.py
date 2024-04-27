class Solution:
    def add(self, n, x=0):
        return (n*(n+1)/2 - x*(x-1)/2)
    def pivotInteger(self, n: int) -> int:
        arr = []
        flag = 0
        if n == 1:
            return 1
        for i in range(1, n+1):
            if self.add(i) == self.add(n, i):
                flag = 1
                break
        return i if flag == 1 else -1

s = Solution()
print(s.pivotInteger(8))