
class Solution:
    def dominantIndex(self, nums) -> int:
        lar = -float('inf')
        second = -float('inf')

        for i in nums:
            if lar < i:
                lar = i
        for i in nums:
            if i == lar:
                continue 
            elif second < i:
                second = i
        return 1 if second*2 <= lar else -1

s = Solution()
print(s.dominantIndex([1,2,3,4]))