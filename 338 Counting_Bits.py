class Solution:
    def count_bits(self, s):
        count = 0
        for i in s:
            if i == "1":
                count += 1
        return count
    def countBits(self, n: int):
        final_ans = []
        for i in range(n+1):
            c = self.count_bits(str(bin(i)))
            final_ans.append(c)
        return final_ans

if __name__ == "__main__":
    s = Solution()
    s.countBits(4)