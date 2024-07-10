class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        i, j = 0,0
        s_set = []
        max_len = 0
        while j != len(s):
            if s[j] not in s_set:
                # print(s[j])
                s_set.append(s[j])
                max_len = max(max_len, len(s_set))
                j += 1
            elif s[j] in s_set:
                s_set.pop(0)
                i += 1
        return max_len
        
if __name__ == "__main__":
    s = Solution()
    k = s.lengthOfLongestSubstring("pwwkew")
    print(k)