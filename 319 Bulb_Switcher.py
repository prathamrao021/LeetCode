class Solution:
    def bulbSwitch(self, n: int) -> int:
        count_sqrt = 0
        i = 1
        while i*i <= n:
            count_sqrt += 1
            i += 1
        return count_sqrt
if __name__ == "__main__":
    s = Solution()
    print(s.bulbSwitch(0))