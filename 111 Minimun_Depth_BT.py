class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calc_min_depth(self, root, depth):

        if root.right != None and root.left == None:
            depth = self.calc_min_depth(root.right, depth)
            depth += 1
            return depth
        if root.left != None and root.right != None:
            depth = min(self.calc_min_depth(root.right, depth), self.calc_min_depth(root.left, depth))
            depth += 1
            return depth
        if root.left != None and root.right == None:
            depth = self.calc_min_depth(root.left, depth)
            depth += 1
            return depth
        if root.left == None and root.right == None:
            return 1
    def minDepth(self, root):
        if root == None:
            return 0
        depth = 0
        depth = self.calc_min_depth(root, 0)
        return depth

node5 = TreeNode(5)
node4 = TreeNode(4, node5)
node3 = TreeNode(3, node4)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, node2)
s = Solution()
print(s.minDepth(node1))


'''class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return 1+self.minDepth(root.right)
        if root.left != None and root.right != None:
            return 1+min(self.minDepth(root.right), self.minDepth(root.left))
        if root.left != None and root.right == None:
            return 1+self.minDepth(root.left)'''