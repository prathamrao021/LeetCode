class Solution:
    def isPlaindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False
        
    def calcualte(self, s, temp):
        if s == "":
            self.ans.append(temp)
        n = len(s)
        for i in range(1,n+1):
            if self.isPlaindrome(s[0:i]):
                self.calcualte(s[i:],temp+[s[0:i]])
    def partition(self, s):
        temp= []
        self.ans = []
        self.calcualte(s,temp)
        return self.ans

if __name__ == "__main__":
    s = Solution()
    s.partition('aab')