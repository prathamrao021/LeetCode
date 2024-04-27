# Definition for a binary tree node.
# DEBUG it...................
# focus on check_valid_swap function and recoverTree function
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
        self.node1 = None
        self.node2 = None


    def check_valid_swap(self, root):
        if root is None:
            return
        
        #In_order traversal
        self.check_valid_swap(root.left)

        if self.prev and self.prev.val > root.val:
            if self.node1 is None:
                self.node1 = self.prev
            self.node2 = root

        self.prev = root

        self.check_valid_swap(root.right)

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

    def recoverTree(self, root):
        self.check_valid_swap(root)
        # if self.node1 and self.node2:
        self.node1.val, self.node2.val = self.node2.val, self.node1.val



s = Solution()

#testcase 1
node2 = TreeNode(2)
node4 = TreeNode(4, node2)
node1 = TreeNode(1)
node3 = TreeNode(3, node1, node4)
s.recoverTree(node3)
s.print_tree(node3)

#testcase 2
# node1 = TreeNode(1)
# node3 = TreeNode(3)
# node2 = TreeNode(2, node3, node1)
# s.recoverTree(node2)
# s.print_tree(node2)

# testcase3
# node2 = TreeNode(2)
# node3 = TreeNode(3, None, node2)
# node1 = TreeNode(1, node3)
# s.recoverTree(node1)
# s.print_tree(node1)

# testcase4
# node2 = TreeNode(2)
# node3 = TreeNode(3,None,node2)
# node1 = TreeNode(1,None,node3)
# s.recoverTree(node1)
# s.print_tree(node1)

#testcase5
# node1 = TreeNode(1)
# node2 = TreeNode(2, None, node1)
# s.recoverTree(node2)
# s.print_tree(node2)