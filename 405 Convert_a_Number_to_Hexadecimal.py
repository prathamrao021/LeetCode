class Solution:
    def toHex(self, num: int) -> str:
        neg = False
        if num < 0:
            neg = True
        ans = ''
        if not neg:
            while num > 0:
                x = num%16
                if x < 10:
                    ans = str(x) + ans
                else:
                    ans = chr(97+(x-10))  +ans
                num = num // 16
        else:
            num += 1
            ans = str(hex((num+int('ffffffff',16))))[2:]
        return ans

if __name__ == "__main__":
    s = Solution()
    k = s.toHex(-3)
    print(k)