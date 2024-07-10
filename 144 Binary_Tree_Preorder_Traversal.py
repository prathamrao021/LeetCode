import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calculate_preorder(self, node, ans):
        ans.append(node.val)
        if node.left != None:
            ans = self.calculate_preorder(node.left, ans)
        if node.right != None:
            ans= self.calculate_preorder(node.right, ans)
        return ans
    def preorderTraversal(self, root):
        ans = []
        ans = self.calculate_preorder(root, ans)
        return(ans)

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
if __name__ == "__main__":
    s = Solution()
    t3 = TreeNode(3)
    t2 = TreeNode(2,t3)
    t1 = TreeNode(1, None, t2)
    s.print_tree(t1)
    k = s.preorderTraversal(t1)
    print(k)
