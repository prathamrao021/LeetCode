class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry_ans  = 0
        a_ans = 0
        b_ans = 0

        a_ans = bin(a)[2:]
        b_ans = bin(b)[2:]

        while len(a_ans) < len(b_ans):
            a_ans = "0"+a_ans
        while len(a_ans) > len(b_ans):
            b_ans = "0"+b_ans
        

        print(bin(a), bin(b))
        bin_ans = ""

        for i in range(len(a_ans)-1,-1,-1):
            if a_ans[i] == "1":
                if b_ans[i] == "1":
                    if carry_ans:
                        carry_ans = 1
                        bin_ans = "1"+bin_ans
                    else:
                        carry_ans = 1
                        bin_ans = "0"+bin_ans
                else:
                    if carry_ans:
                        carry_ans = 1
                        bin_ans = "0"+bin_ans
                    else:
                        carry_ans = 0
                        bin_ans = "1"+bin_ans
            else:
                if b_ans[i] == "1":
                    if carry_ans:
                        carry_ans = 1
                        bin_ans = "0"+bin_ans
                    else:
                        carry_ans = 0
                        bin_ans = "1"+bin_ans
                else:
                    if carry_ans:
                        carry_ans = 0
                        bin_ans = "1"+bin_ans
                    else:
                        carry_ans = 0
                        bin_ans = "0"+bin_ans
        if carry_ans == 1:
            bin_ans ="1"+bin_ans
        
        return int(bin_ans,2)


if __name__ == "__main__":
    s = Solution()
    print(s.getSum(17,13))