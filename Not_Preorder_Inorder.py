# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calc_tree(self, preoder, inorder, value):
        if len(inorder) == 1:
            node = TreeNode(inorder[0], None, None)
            return node
        root = TreeNode()
        root.val = value
        #find another root for left subtree and right subtree
        root.left = self.calc_tree(preoder, inorder, root)

    def buildTree(self, preorder, inorder):
        root = self.calc_tree(preorder, inorder, preorder[0])
        return root
                
if __name__ == "__main__":
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    s.buildTree(preorder, inorder)

