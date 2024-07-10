class Solution:
    def constructRectangle(self, area: int):
        # min_diff = float('inf')
        length = 0
        width = 0
        for i in range(1,int(area**0.5)+1):
            if area%i == 0:
                width = i
                length = area//i


        return ([length, width])
if __name__ == "__main__":
    s = Solution()
    s.constructRectangle(122122)