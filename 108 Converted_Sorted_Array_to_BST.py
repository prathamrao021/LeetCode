# Definition for a binary tree node.
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if nums == None:
            return None
        if len(nums) == 0:
            return None
        root = self.calculate(nums, 0, len(nums)-1)
        return root

    def calculate(self, nums, start, end):
        if start > end:
            return None
        mid = (start+(end-start)//2)
        parent = TreeNode()
        parent.val = nums[mid]
        parent.left = self.calculate(nums, start, mid-1)
        parent.right = self.calculate(nums, mid+1, end)
        return parent
    
    def print_tree(self, node, indent="", last='updown'):
        nb_space = 10
        if node != None:
            sys.stdout.write(indent)
            if last == 'updown':
                sys.stdout.write('----')
                indent += "     "
            elif last == 'leftright':
                sys.stdout.write(' /-- ')
                indent += "|    "
            else:
                sys.stdout.write(' \\-- ')
                indent += '     ' 
        print(str(node.val))
        if node.left is not None:
            self.print_tree(node.left, indent, 'leftright')
        if node.right is not None:
            self.print_tree(node.right, indent, 'updown')

s = Solution()
k = s.sortedArrayToBST([-10,-3,0,5,9])
s.print_tree(k)