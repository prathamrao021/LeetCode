import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=0, left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def tree_traversal(self,node,p,q):
        if node.val > p.val and node.val > q.val:
            self.tree_traversal(node.left, p, q)
        elif node.val < p.val and node.val < q.val:
            self.tree_traversal(node.right, p, q)
        else:
            self.result = node
        return
    def lowestCommonAncestor(self, root, p, q):
        if p == root or q == root:
            return root
        self.result = TreeNode(0)
        self.tree_traversal(root,p,q)
        return(self.result)
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
    t5 = TreeNode(5)
    t4 = TreeNode(4,t3,t5)
    t0 = TreeNode(0)
    t2 = TreeNode(2,t0,t4)
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t8 = TreeNode(8)
    t6 = TreeNode(6,t2,t8)
    
    s.print_tree(t6)
    k = s.lowestCommonAncestor(t6,t4,t2)
    print(k.val)
