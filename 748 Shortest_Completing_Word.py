class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        alpha_dict = {}
        for i in licensePlate:
            i = i.lower()
            if i.isalpha():
                if alpha_dict.get(i) != None:
                    alpha_dict[i] += 1
                else:
                    alpha_dict[i] = 1
        
        temp_dict = alpha_dict.copy()
        min_len = '5'*16
        check = True
        for word in words:
            temp_dict = alpha_dict.copy()
            check = True
            for i in word:
                if temp_dict.get(i) != None:
                    temp_dict[i] -= 1

            for key,val in temp_dict.items():
                if val > 0:
                    check = False
                    break
            if check and len(min_len) > len(word):
                min_len = word
        return min_len

if __name__ == "__main__":
    s = Solution()
    print(s.shortestCompletingWord("GrC8950",["measure","other","every","base","according","level","meeting","none","marriage","rest"]))