class Solution:
    def merge(self, intervals):
        intervals.sort(key= lambda x: x[0])
        temp = []
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            temp = intervals[i]
            if ans[-1][1] >= temp[0]:
                last = ans.pop()
                if temp[0] > last[0]:
                    temp[0] = last[0]
                if temp[1] < last[1]:
                    temp[1] = last[1]
            ans.append(temp)

        print(ans)
                
                
s = Solution()
s.merge([[1,4],[0,4],[8,10],[15,18]])