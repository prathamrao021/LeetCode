class Solution:
    def numberOfLines(self, widths, s: str):
        if s == "":
            return [0,0]
        count_lines = 1
        max_limit = 0
        for i in s:
            if max_limit + widths[ord(i)-97] > 100:
                max_limit = 0
                count_lines += 1
            
            max_limit += widths[ord(i)-97]
        return [count_lines, max_limit]



if __name__ == "__main__":
    s = Solution()
    k = s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz")
    print(k)