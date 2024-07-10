class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        prev = False
        nex = False
        for i in range(len(flowerbed)):
            if i == 0:
                prev = True
            else:
                prev = False
            
            if i == len(flowerbed):
                nex = True
            else:
                nex = False

            if flowerbed[i] == 1:
                continue
            else:
                if i+1 < len(flowerbed) and flowerbed[i+1] == 0:
                    nex = True
                if i-1 >= 0 and flowerbed[i-1] == 0:
                    prev = True
                if n > 0:
                    if i == 0 and nex:
                        flowerbed[i] = 1
                        n -= 1
                    elif i == len(flowerbed)-1 and prev:
                        flowerbed[i] = 1
                        n -= 1
                    elif prev and nex:
                        flowerbed[i] = 1
                        n -= 1
        return True if n == 0 else False

if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,0,1], 2))