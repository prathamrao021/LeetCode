class Solution:
    def specialArray(self, nums) -> int:
        count = 0
        for i in range(1,len(nums)+1):
            count = 0
            for j in nums:
                if j >= i:
                    count += 1
                print(i, j, count)
            if count == i:
                return i
        return -1
if __name__ == "__main__":
    s = Solution()
    k = s.specialArray([2,4,1,7,8,9,6,5,3])
    print(k)
