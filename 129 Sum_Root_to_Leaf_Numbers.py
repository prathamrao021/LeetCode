# Definition for a binary tree node.
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str_nums(self,node,arb_str):
        # arb_str += str(node.val)
        
        if node.left != None:
            self.str_nums(node.left, arb_str+str(node.val))
        if node.right != None:
            self.str_nums(node.right, arb_str+str(node.val))

        if node.right == None and node.left == None:
            arb_str += str(node.val)
            self.result += int(arb_str)
        
    def sumNumbers(self, root):
        if root == None:
            return 0
        self.result = 0
        arb_str = ''
        self.str_nums(root,arb_str)
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
    s  = Solution()
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1 = TreeNode(1,t2,t3)
    s.print_tree
    k = s.sumNumbers(t1)
    print(k)