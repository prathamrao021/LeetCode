class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        arr = ""
        for i in s:
            if i != "-":
                arr+=i
        
        ans = ""
        count = 0
        for i in range(len(arr)-1,-1,-1):
            if arr[i].isalpha():
                ans = arr[i].upper()+ans
            else:
                ans = arr[i]+ans
            count += 1
            if count == k and i != 0:
                ans  = "-" + ans
                count = 0
        return(ans)

s = Solution()
print(s.licenseKeyFormatting("5F3Z-2e-9-w",4))