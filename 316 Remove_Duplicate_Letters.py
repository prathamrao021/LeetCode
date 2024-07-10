#using stack, set and map


import collections
class Solution:
    def removeDuplicateLetters(self, s: str):
        last_occ_map = dict()
        for i in range(len(s)):
            last_occ_map[s[i]] = i

        seen = set()
        order = collections.deque()

        for i in range(len(s)):
            if s[i] in seen:
                continue
                
            while order and order[-1] > s[i] and last_occ_map[order[-1]] > i:
                seen.remove(order.pop())
            
            if s[i] not in seen:
                seen.add(s[i])
                order.append(s[i])
        
        ans = ''.join(order)
        return(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters("ecbacba"))