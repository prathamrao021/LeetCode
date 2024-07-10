class Solution:
    def intToRoman(self, num):
        int_to_rom = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
        i = 0
        ans =''
        while num != 0:
            if num - int_to_rom[i][0] < 0:
                i += 1
            else:
                ans = ans+int_to_rom[i][1]
                num -= int_to_rom[i][0]
        return (ans)
if __name__ == "__main__":
    s = Solution()
    k = s.intToRoman(3749)
    print(k)
