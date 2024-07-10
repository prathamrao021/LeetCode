class Solution:
    def validPalindrome(self, s: str) -> bool:
        s1 = s[::-1]
        n = len(s)-1
        count = 0
        for i in range(len(s)):
            if s[i] != s1[i]:
                print(i,n-i,s,s1)
                print(s[:i]+s[i+1:],s1[:n-i]+s1[n-i+1:])
                if s[:i]+s[i+1:] == s1[:n-i]+s1[n-i+1:]:
                    return True
                else:
                    if count ==0 :
                        count += 1
                        continue
                    else:
                        return False
        return True

s = Solution()
print(s.validPalindrome('eccer'))