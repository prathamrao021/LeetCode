class Solution:
    def reverseVowels(self, s: str) -> str:
        if s == " ":
            return s
        s = s.strip()
        if len(s) == 1:
            return s
        i, j = 0, len(s)-1
        vowels_set = set(['A','E','I','O','U','a','e','i','o','u'])
        while i <= j:
            while i < len(s) and s[i] not in vowels_set:
                i+=1
            while j >= 0 and s[j] not in vowels_set:
                j -= 1
            if i > j:
                break
            # print(s[i],s[j])
            s = list(s)
            s[i],s[j] = s[j],s[i]
            s = "".join(s)
            i+=1
            j-=1
        return s
if __name__ == "__main__":
    s = Solution()
    s.reverseVowels(".,")