class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False

        while n != 0:
            if n%4 == 0:
                n /= 4
            elif n == 1:
                return True
            else:
                return False

if __name__ == "__main__":
    s = Solution()
    k = s.isPowerOfFour(16)
    print(k)