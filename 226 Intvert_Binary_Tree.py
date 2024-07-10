class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverse_tree(self, node):
        if node == None:
            return None
        # temp = node.right
        # node.right = node.left
        # node.left = temp
        temp = node.right
        node.right = self.reverse_tree(node.left)
        node.left = self.reverse_tree(temp)
        return node
    def invertTree(self, root):
        if root == None:
            return None
        root = self.reverse_tree(root)
        return root

if __name__ == "__main__":
    s = Solution()
    t3 = TreeNode(3)
    t2 = TreeNode(2)
    t1  =TreeNode(1,t2)

    s.invertTree(t1)