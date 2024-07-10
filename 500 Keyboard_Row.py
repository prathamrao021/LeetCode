class Solution:
    def findWords(self, words):
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        result = []
        set_row = -1
        check = True
        #put check to check if it was in same row.
        for word in words:
            set_row = -1
            check = True
            for i in word:
                if set_row == -1:
                    if i.lower() in first_row:
                        set_row = 0
                    elif i.lower() in second_row:
                        set_row = 1
                    elif i.lower() in third_row:
                        set_row = 2
                elif set_row == 0:
                    if i.lower() not in first_row:
                        check = False
                        break
                elif set_row == 1:
                    if i.lower() not in second_row:
                        check = False
                        break
                elif set_row == 2:
                    if i.lower() not in third_row:
                        check = False
                        break
            if check:
                result.append(word)
        return result

if __name__ == "__main__":
    s = Solution()
    k = s.findWords(["Hello","Alaska","Dad","Peace"])
    print(k)