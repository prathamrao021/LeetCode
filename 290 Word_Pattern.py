import collections
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_dict = collections.defaultdict(set)
        word_dict = collections.defaultdict(set)
        arr = s.split(" ")
        if len(arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            word_dict[arr[i]].add(pattern[i])
            char_dict[pattern[i]].add(arr[i])
        
        if len(char_dict) == len(word_dict):
            for i in word_dict.keys():
                if len(word_dict[i]) == 1:
                    continue
                else: return False
        else:
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    s.wordPattern("aba","dog cat cat")