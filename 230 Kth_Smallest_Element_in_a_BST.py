import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calculate(self, node):
        if node.left != None:
            self.calculate(node.left)
            self.steps -= 1
        
        if self.steps == 0:
            self.ans = node
            return 

        if node.right != None:
            self.steps -= 1
            self.calculate(node.right)
        return
    
    def kthSmallest(self, root, k: int) -> int:
        self.ans = TreeNode()
        self.steps = k-1
        self.calculate(root)
        return(self.ans.val)


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
    t3 = TreeNode(3,t2,t4)
    t6 = TreeNode(6)
    t5 = TreeNode(5,t3,t6)

    s.print_tree(t5)
    k = s.kthSmallest(t5,3)
    print(k)

        