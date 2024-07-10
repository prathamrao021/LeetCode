class NumArray:

    def __init__(self, nums):
        self.arr = nums
        self.dp = [0 for _ in range(len(nums)+1)]

        for i in range(len(self.dp)-1):
            if i == 0:
                self.dp[i+1] = nums[i]
            else:
                self.dp[i+1] = self.dp[i] + nums[i]


    def update(self, index: int, val: int) -> None:
        diff = val - (self.dp[index+1] - self.dp[index])

        for i in range(index+1, len(self.dp)):
            self.dp[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        return self.dp[right+1] - self.dp[left]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,3,5])
param_2 = obj.sumRange(0,2)
print(param_2)
obj.update(1,2)
param_3 = obj.sumRange(0,2)
print(param_3)