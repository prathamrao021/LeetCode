# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        root = TreeNode()
        for i in range(len(preorder)):
            if i == 0:
                root.val = preorder[i]
            if i > 0:
                pass
        