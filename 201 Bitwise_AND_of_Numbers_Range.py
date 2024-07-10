# class Solution:
#     def power_2(self, n):
#         if n & n-1 == 0:
#             return True
#         else:
#             return False
#     def closest_power_2(self,n):
#         x = 0
#         while 2**x < n:
#             x += 1
#         return 2**(x-1)
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         if left == right:
#             return left
#         and_ans = left
#         for i in range(left+1, right+1):
#             if self.power_2(i):
#                 return 0
#             else:
#                 and_ans = and_ans & i
#         return and_ans

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt

if __name__ == "__main__":
    s = Solution()
    k = s.rangeBitwiseAnd(5,7)
    print(k)