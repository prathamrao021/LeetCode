class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == len(s):
            return s[::-1]
        front = 0
        rear = 0
        ans = ""
        reverse = True
        while rear < len(s):
            while rear != front + k:
                rear += 1
            if rear >= len(s):break
            s1 = s[front:rear]
            if reverse:
                ans += s1[::-1]
                front = rear
                reverse = not reverse
            else:
                ans += s1
                reverse = not reverse
                front = rear
        if len(ans) != len(s):
            ans += s[front:]
        return(ans)

s = Solution()
print(s.reverseStr("abcd",4))