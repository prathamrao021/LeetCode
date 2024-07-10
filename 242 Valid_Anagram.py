class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_to_store = {}
        for i in s:
            if dict_to_store.get(i) == None:
                dict_to_store[i] = 1
            else:
                dict_to_store[i] += 1
        
        for i in t:
            if dict_to_store.get(i) == None:
                return False
            else:
                dict_to_store[i] -= 1
        
        for i in dict_to_store.values():
            if i != 0:
                return False
        return True

s = Solution()
s.isAnagram("anagram","nagaram")
