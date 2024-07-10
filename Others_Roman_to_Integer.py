class Solution:
    def romanToInt(self, s: str) -> int:
        # int_to_rom = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
        rom = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        arr_int = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        j = 0
        ans = 0
        while j != len(s):
            if j<len(s)-1 and s[j:j+2] in rom:
                print(arr_int[rom.index(s[j:j+2])],s[j:j+2])
                ans += arr_int[rom.index(s[j:j+2])]
                j+=2
            else:
                print(arr_int[rom.index(s[j])],s[j])
                ans += arr_int[rom.index(s[j])]
                j+=1
        return ans
if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MXC"))