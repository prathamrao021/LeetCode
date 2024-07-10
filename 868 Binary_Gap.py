class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        count = 0
        max_count = 0
        for i in range(len(binary)):
            if binary[i] == '0':
                count += 1
            else:
                count = 0
            max_count = max(count, max_count)
        return max_count+1

if __name__ == "__main__":
    s = Solution()
    s.binaryGap(22)