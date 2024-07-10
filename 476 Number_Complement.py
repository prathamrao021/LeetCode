class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        new_binary = ""
        for i in range(2,len(binary)):
            if binary[i] == "1":
                new_binary += "0"
            else:
                new_binary += "1"
        ans = 0
        # if len(new_binary) == 1:
        #     return int(new_binary,2)
        # for i in new_binary:
        #     if i == "0":
        #         new_binary = new_binary[1:]
        #     else:
        #         break
        return (int(new_binary,2))

if __name__ == "__main__":
    s = Solution()
    k = s.findComplement(5)
    print(k)