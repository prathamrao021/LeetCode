# class Solution:
#     def calculate(self, nums, target_left, temp):
#         if target_left < 0 :
#             return
#         elif target_left == 0:
#             self.count += 1
#             return
#         else:
#             for i in range(len(nums)):
#                 self.calculate(nums, target_left-nums[i], temp+[nums[i]])
#     def combinationSum4(self, nums, target):
#         temp = []
#         target_left = target
#         self.count = 0
#         for i in range(len(nums)):
#             self.calculate(nums, target_left-nums[i], temp+[nums[i]])
#         print(self.count)
#         return self.count

class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        # Initialize an array dp where dp[i] represents the number of combinations to make sum 'i'.
        dp = [0] * (target + 1)
        
        # There is one way to make sum 0, which is by not selecting any number.
        dp[0] = 1
        
        # Iterate through the possible target sums from 1 to target.
        for currentSum in range(1, target + 1):
            for numIndex in range(0, len(nums)):
            # Iterate through the given numbers in nums.
                currentNum = nums[numIndex]
                # Check if subtracting currentNum from currentSum results in a non-negative value.
                if currentSum - currentNum >= 0:
                    # dp[i] can be achieved by adding the combination count at dp[i - currentNum].
                    dp[currentSum] += dp[currentSum - currentNum]
            print(dp)
            
        # The final result is stored in dp[target].
        return dp[target]
if __name__ == "__main__":
    s = Solution()
    k = s.combinationSum4([1,2,3],4)
    print(k)
