import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_table = collections.Counter(s)
        ans = 0
        single_once = True
        if len(freq_table) == 1:
            return (s.count(s[0]))
        if len(freq_table) == 2:
            return (len(s))
        for i in freq_table.keys():
            if freq_table[i]%2 == 0:
                ans += freq_table[i]
            elif freq_table[i] > 1:
                ans += freq_table[i]-1
            elif single_once and freq_table[i]%2 == 1:
                single_once = False
                ans += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    k = s.longestPalindrome("ccc")
    print(k)