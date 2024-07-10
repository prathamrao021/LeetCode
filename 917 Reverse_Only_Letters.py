class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        low = 0
        high = len(s)-1
        s = list(s)
        while low < high:
            while low < high and not s[low].isalpha():
                low += 1
            while low < high and not s[high].isalpha():
                high -=1
            s[low], s[high] =  s[high], s[low]
            low += 1
            high -= 1
        return "".join(s)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))