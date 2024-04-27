# 98. Validate Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self, node, range_min, range_max):
        if node == None:
            return True
        if node.val >= range_max or node.val <= range_min:
            return False
        else:
            return self.check(node.left, range_min, node.val) and self.check(node.right, node.val, range_max)

    def isValidBST(self, root):
        return self.check(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    sol = Solution()
    print(sol.isValidBST(node1))
