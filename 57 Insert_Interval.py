class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals = intervals[:i]+[newInterval]+intervals[i:]
                break
            if i == len(intervals)-1:
                intervals.append(newInterval)
        print(intervals)
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
        return ans

s = Solution()
print(s.insert([[1,5]], [2,7]))