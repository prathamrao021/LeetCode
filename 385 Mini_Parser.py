class Solution:
    def deserialize(self, s: str):
        if not s: return list()
        if not s.startswith("["): return int(s) # integer 
        ans = list()
        s = s[1:-1] # strip outer "[" and "]"
        if s: 
            ii = op = 0 
            for i in range(len(s)): 
                if s[i] == "[": op += 1
                if s[i] == "]": op -= 1
                if s[i] == "," and op == 0: 
                    ans.append(self.deserialize(s[ii:i]))
                    ii = i+1
            ans.append(self.deserialize(s[ii:i+1]))
        return ans 

if __name__ == "__main__":
    s = Solution()
    print(s.deserialize("[123,[456,[789]]]"))