class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        ans = 0
        for i in range(1,len(timeSeries)):
            if timeSeries[i-1] + duration - 1 >= timeSeries[i]:
                ans += (timeSeries[i]-timeSeries[i-1])
            else:
                ans += duration
        
        ans += duration 
        return(ans)
    
if __name__ == "__main__": 
    s = Solution()
    k = s.findPoisonedDuration([1,4],2)
    print(k)