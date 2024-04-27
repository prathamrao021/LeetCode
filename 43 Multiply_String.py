# reference number = 0
# reference ascii = 48
class Solution:
    def decode(self, num1):
        ans = 0
        for i in range(len(num1)):
            ans = ans*10 + (ord(num1[i]) - ord("0"))
        return ans
    def multiply(self, num1, num2):
        n1 = self.decode(num1)
        n2 = self.decode(num2)
        return (str(n1*n2))

if __name__ == "__main__":
    s = Solution()
    k = s.multiply("123","456")
    print(k)
