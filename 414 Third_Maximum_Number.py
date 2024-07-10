import heapq
class Solution:
    def thirdMax(self, nums) -> int:
        nums = set(nums)
        max_heap = []
        for i in nums:
            heapq.heappush(max_heap,(-i))
        
        length = len(max_heap)
        for j in range(3):
            ans = -1*(heapq.heappop(max_heap))
            if length < 3:
                return ans
        return ans

if __name__ == "__main__":
    s = Solution()
    k = s.thirdMax([2,1])
    print(k)