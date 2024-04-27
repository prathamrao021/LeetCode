class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return ([1])
        elif rowIndex == 1:
            return ([1,1])
        pre_arr = [1,1]
        curr_arr = []
        for i in range(3,rowIndex+2):
            for j in range(i):
                if j == 0 or j == len(pre_arr):
                    curr_arr.append(1)
                else:
                    curr_arr.append(pre_arr[j-1]+pre_arr[j])
            pre_arr = curr_arr
            curr_arr = []
        return(pre_arr)

if __name__ == "__main__":
    s = Solution()
    s.getRow(3)