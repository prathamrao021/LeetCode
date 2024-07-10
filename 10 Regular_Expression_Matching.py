import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s1 = re.sub(r'\*{2,}',"*",p)
        arr = re.findall(s1,s)
        print(arr)
        for i in arr:
            if i == s:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("a",".*..a*"))