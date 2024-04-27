# Definition for a binary tree node.
def build_tree(nodes, index=0):
    if index < len(nodes):
        if nodes[index] is None:
            return None
        else:
            root = TreeNode(nodes[index])
            root.left = build_tree(nodes, 2 * index + 1)
            root.right = build_tree(nodes, 2 * index + 2)
            return root
    return None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calc_path_val(self, root, targetSum, path_val):
        if root == None:
            return False
        path_val += root.val
        if path_val == targetSum and root.right == None and root.left == None:
            return True
        if path_val == targetSum and (root.right != None or root.left != None):
            leftpath = self.calc_path_val(root.left, targetSum, path_val)
            rightpath = self.calc_path_val(root.right, targetSum, path_val)
            if leftpath or rightpath:
                return True
        elif path_val != targetSum:
            leftpath = self.calc_path_val(root.left, targetSum, path_val)
            rightpath = self.calc_path_val(root.right, targetSum, path_val)
            if leftpath or rightpath:
                return True
        
    def hasPathSum(self, root, targetSum):
        if root == None:
            return 0
        path_val = 0
        exists = self.calc_path_val(root, targetSum, path_val)
        return exists

s = Solution()
# node7 = TreeNode(7)
# node2 = TreeNode(2)
# node11 = TreeNode(11, node7, node2)
# node4 = TreeNode(4, node11)
# node13 = TreeNode(13)
# node1 = TreeNode(1)
# node4_2 = TreeNode(4, None, node1)
# node8 = TreeNode(8, node13, node4_2)
# node5 = TreeNode(5, node4, node8)

# noden3 = TreeNode(-3)
# noden2 = TreeNode(-2,noden3)

root = build_tree([1,-2,-3,1,3,-2,None,-1])
# print(root.val)
print(s.hasPathSum(root, -1))