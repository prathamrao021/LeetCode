import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        vals = []
        # Easy recursive Inorder Traversal to get our values to insert.
        def inord(node):
            if not node:
                return
            inord(node.left)
            vals.append(node.val)
            inord(node.right)
            
        inord(root)
        # Create a new tree to return.
        tree = TreeNode(val=vals[0])
		# Use a sentinel so we dont lose our tree location in memory.
        tmp = tree
		# Iterate through our vals, creating a new right node with the current val.
        for i in vals[1:]:
            tmp.right = TreeNode(val=i)
			# Move the sentinel to the next node.
            tmp = tmp.right
            
        return tree
    
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
    t1 = TreeNode(1)
    t2 = TreeNode(2,t1)
    t4 = TreeNode(4)
    t3 = TreeNode(3, t2,t4)
    
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t8 = TreeNode(8,t7,t9)
    t6 = TreeNode(6,None, t8)
    
    t5 = TreeNode(5,t3,t6)
    
    s.print_tree(t5)
    root = s.increasingBST(t5)
    s.print_tree(root)