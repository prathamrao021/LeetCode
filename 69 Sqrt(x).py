class Solution:
    def mySqrt(self, x) -> int:
        low = 1
        high = x
        while low <= high:
            mid = low + ((high - low) //2)
            print(high, low, mid)
            if mid == x//mid:
                return mid
            elif (x//mid < mid):
                high = mid-1
            else:
                low = mid+1
        print(high)
s = Solution()
s.mySqrt(8)