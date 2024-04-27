class Solution:
    def groupAnagrams(self, strs):
        ana_dict = {}
        ans = [[]]
        i = 0
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in ana_dict:
                ana_dict[sorted_word] = []
            ana_dict[sorted_word].append(word)
        return list(ana_dict.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))