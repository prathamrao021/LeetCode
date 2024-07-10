import heapq
import math
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         ans = [0]
#         for i in range(1,len(citations)+1):
#             count = 0
#             for j in range(len(citations)):
#                 if citations[j] >= i:
#                     count += 1
#             if count >= i:
#                 ans.append(i)
#         return ans[-1]
class Solution:
    def hIndex(self, citations) -> int:
        heapq.heapify(citations)
        mx = -math.inf
        count = len(citations)
        while len(citations) > 0:
            val = heapq.heappop(citations)
            print(val, count, "....")
            mx = max(mx, min(count, val))
            count -= 1
        return mx

if __name__ == "__main__":
    s = Solution()
    s.hIndex([3,0,6,1,5])