class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        max_child = len(g)
        max_cook = len(s)
        i,j = 0,0
        count = 0 
        while i < len(g):
            while j < len(s):
                if len(g) == 0:
                    break
                if g[i] > s[j]:
                    j += 1
                elif g[i] <= s[j]:
                    count += 1
                    g.remove(g[i])
                    s.remove(s[j])
            i+=1
        return count

if __name__ == "__main__":
    s = Solution()
    k = s.findContentChildren([1,2],[1,2,3])
    print(k)