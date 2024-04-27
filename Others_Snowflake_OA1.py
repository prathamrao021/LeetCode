class Solution:
    def Combinations(self, min, maxU, s):
        hashmap = {}
        for i in range(min, maxU+1):
            for j in range(len(s)-i+1):
                if s[j:j+i] not in hashmap:
                    hashmap[s[j:j+i]] = 1
                else:
                    hashmap[s[j:j+i]] += 1
        max_freq = list(hashmap.values())
        print(hashmap)
        return(max(max_freq))

if __name__ == "__main__":
    s = Solution()
    print(s.Combinations(2, 3, 'abcee'))