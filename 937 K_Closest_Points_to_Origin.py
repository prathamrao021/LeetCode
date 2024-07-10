import collections
import heapq
class Solution:
    def kClosest(self, points, k: int):
        priority_que = []
        for i in range(len(points)):
            dis = points[i][0]**2 + points[i][1]**2 
            heapq.heappush(priority_que, (dis,[points[i][0],points[i][1]]))

        result = []
        for i in range(k):
            result.append(heapq.heappop(priority_que)[1])
        return result
        

if __name__ == "__main__":
    s = Solution()
    s.kClosest([[1,3],[-2,2]],1)