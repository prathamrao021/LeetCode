class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while True:
            if n == 1: return True
            if n%5 == 0:
                n /= 5
            elif n%3 == 0:
                n /= 3
            elif n%2 ==0:
                n/=2
            else:
                return False

if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(6))