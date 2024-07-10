from collections import deque
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp_queu = deque(nums)
        m = len(nums)-k

        for i in range(m):
            curr = nums.pop(0)
            nums.append(curr)
        # nums = list(nums)
        print(nums)

if __name__ == "__main__":
    s = Solution()
    s.rotate([1,2,3,4,5,6,7], 3)