class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ans = ""
        cor_pos = {}
        guess_hashtable = {}
        for i in range(len(guess)):
            # guess_hashtable.add(guess[i])
            if secret[i] == guess[i]:
                cor_pos[i] = secret[i]
            elif guess_hashtable.get(guess[i]) == None:
                guess_hashtable[guess[i]] = 1
            else:
                guess_hashtable[guess[i]] += 1
        ans += str(len(cor_pos))+"A"
        
        cor_digit = 0
        for i in range(len(secret)):
            if cor_pos.get(i) != None:
                continue
            elif guess_hashtable.get(secret[i]) != None and guess_hashtable[secret[i]] > 0:
                cor_digit += 1
                guess_hashtable[secret[i]] -= 1
        ans += str(cor_digit) + "B"
        
        return ans

if __name__ == "__main__":
    s = Solution()
    k = s.getHint("1123","0111")
    print(k)