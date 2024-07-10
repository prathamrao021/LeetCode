class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = 0
        i=0
        while len(num1) != 0:
            ans += int(num1[-1])*(10**i)
            num1 = num1[:-1]
            i+=1
        i=0
        while len(num2) != 0:
            ans += int(num2[-1])*(10**i)
            num2 = num2[:-1]
            i+=1
        return str(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.addStrings('11','123'))