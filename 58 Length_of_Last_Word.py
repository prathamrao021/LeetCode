class Solution:
    def lengthOfLastWord(self, s):
        ending_ind = len(s) - 1
        starting_ind = len(s) - 1
        set_ending = False

        for i in range(len(s) - 1, -1, -1):
            if s[i]==" ":
                if set_ending:
                    starting_ind = i + 1
                    return ending_ind - starting_ind + 1
                ending_ind -= 1
                starting_ind -= 1
            elif s[i].isalpha():
                if set_ending:
                    starting_ind -= 1
                    continue
                else:
                    set_ending = True
                    starting_ind -= 1
        if starting_ind == -1:
            return ending_ind + 1
        return ending_ind - starting_ind + 1

        
        
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("a"))
    