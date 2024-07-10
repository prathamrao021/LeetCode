class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans = ans+((26**(len(columnTitle)-i-1))*(ord(columnTitle[i])-64))
        return(ans)
if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("AB")) # 28