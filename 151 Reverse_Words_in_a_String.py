class Solution:
    def reverseWords(self, s: str) -> str:
        trim = s.strip()
        reverse = trim[::-1]
        countinous_space = 0
        inter_words = ""

        final_ans = ''
        for i in range(len(reverse)):
            if reverse[i] == " ":
                final_ans += inter_words[::-1]
                inter_words = ''
                if countinous_space == 1:
                    continue
                else:
                    final_ans += " "
                    countinous_space += 1
            else:
                countinous_space = 0
                inter_words += reverse[i]
        final_ans += inter_words[::-1]
        return(final_ans)


if __name__ == "__main__":
    s = Solution()

    k = s.reverseWords("a good   example")
    print(k)