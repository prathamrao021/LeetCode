class Solution:
    def shortestToChar(self, s: str, c: str):
        n = len(s)
        first_occ = 0
        last_occ = 0
        k = 0
        ans = [0]*n
        for i in range(0, n):
            if s[i] == c:
                first_occ = i
                break
        for i in range(n-1, -1,-1):
            if s[i] == c:
                last_occ = i
                break
        
        for i in range(first_occ, n):
            if s[i] == c:
                k = 0
                ans[i] = 0
            else:
                k+=1
                ans[i] = k
        
        for i in range(last_occ,-1,-1):
            if s[i] == c:
                k = 0
                ans[i] = 0
            else:
                k+=1
                if i < first_occ:
                    ans[i] = k
                else:
                    ans[i] = min(k, ans[i])
        return(ans)

if __name__ == "__main__":
    s = Solution()
    s.shortestToChar("loveleetcode", 'e')