from statistics import *
from math import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        hash = {}
        all_chars = []
        highest_count = 0
        total_of_other_chars = 0
        result = ''
        all_visited = []
        for i in range(len(s)):
            hash[s[i]] = 0
        
        for i in range(len(s)):
            hash[s[i]] += 1

        hash = list(sorted(hash.items(), key=lambda x: x[1], reverse=True))

        for key,val in hash:
            highest_count = max(highest_count, val)

        if highest_count == 1:
            return s

        # for key,val in hash:
        #     if val != highest_count:
        #         total_of_other_chars += val
        total_of_other_chars = len(s)-highest_count
        if highest_count > total_of_other_chars+1:
            return ""
        else:
            # print(highest_count,total_of_other_chars)
            total_of_other_chars += highest_count
            j = 0
            k = 1
            mean_val = 0
            for i in hash:
                mean_val += i[1]

            mean_val = ceil(mean_val/len(hash))

            # print(even,odd)
            print(hash, total_of_other_chars+1, highest_count,mean_val)
            # for i in range(total_of_other_chars+1):
            even = list(hash.pop(0))
            for l in range(len(hash)):
                if hash[l][1] <= mean_val:
                    break
            # print(i, hash)
            odd = list(hash.pop(l))
            #     if i%2 == 0:
            #         if hash[j][1] > 0:
            #             result += hash[j][0]
            #             hash[j] = (hash[j][0], hash[j][1]-1)
            #         if hash[j][1] == 0 and j+2 < len(hash)-1:
            #             j += 2
            #     else:
            #         if hash[k][1] > 0:
            #             result += hash[k][0]
            #             hash[k] = (hash[k][0], hash[k][1]-1)
            #         if hash[k][1] == 0 and k+2 < len(hash)-1:
            #             k += 2

            for i in range(len(s)+1):
                if i % 2 == 0:
                    if even[1] > 0:
                        result += even[0]
                        even[1] -= 1
                    if even[1] == 0:
                        try:
                            even = list(hash.pop(0))
                        except:
                            pass
                else:
                    if odd[1] > 0:
                        result += odd[0]
                        odd[1] -= 1
                    if odd[1] == 0:
                        try:
                            for l in range(len(hash)):
                                if hash[l][1] <= mean_val:
                                    break
                            odd = list(hash.pop(l))
                        except:
                            pass
        return(result)

        
if __name__ == '__main__':
    s = Solution()
    k = s.reorganizeString("gpneqthatplqrofqgwwfmhzxjddhyupnluzkkysofgqawjyrwhfgdpkhiqgkpupgdeonipvptkfqluytogoljiaexrnxckeofqojltdjuujcnjdjohqbrzzzznymyrbbcjjmacdqyhpwtcmmlpjbqictcvjgswqyqcjcribfmyajsodsqicwallszoqkxjsoskxxstdeavavnqnrjelsxxlermaxmlgqaaeuvneovumneazaegtlztlxhihpqbajjwjujyorhldxxbdocklrklgvnoubegjrfrscigsemporrjkiyncugkksedfpuiqzbmwdaagqlxivxawccavcrtelscbewrqaxvhknxpyzdzjuhvoizxkcxuxllbkyyygtqdngpffvdvtivnbnlsurzroxyxcevsojbhjhujqxenhlvlgzcsibcxwomfpyevumljanfpjpyhsqxxnaewknpnuhpeffdvtyjqvvyzjeoctivqwann")
    print(k)