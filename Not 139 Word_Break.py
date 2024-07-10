class Solution:
    def calculate(self, s, wordDict):
        if s == "":
            self.check = True
            return True
        n = len(s)
        i = 0
        while i<=n:
            for j in wordDict:
                if s[i:].startswith(j):
                    
                    found = self.calculate(s[i+len(j):], wordDict)
                    if found:
                        return True
            if i != n:
                return False
                    
    def wordBreak(self, s: str, wordDict) -> bool:
        self.check = False
        k = self.calculate(s, wordDict)
        return(k)
        
if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("cars",["car","ca","rs"]))
        