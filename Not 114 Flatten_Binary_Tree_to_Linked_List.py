import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        node_right = root
        temp_right = None
        if root.right:
            temp_right = root.right
        if root.left:
            root.right,node_right = self.flatten(root.left)
            root.left = None
        if temp_right:
            node_right.right,node_right = self.flatten(temp_right)
        
        return (root,node_right)

        

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
    t1 = TreeNode(3)
    t2 = TreeNode(4)
    t3 = TreeNode(2,t1,t2)
    t4 = TreeNode(6)
    t5 = TreeNode(5,None,t4)
    t6 = TreeNode(1,t3,t5)
    s.print_tree(t6)
    root,x = s.flatten(t6)
    s.print_tree(root) 