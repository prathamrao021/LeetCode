import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if inorder:
            index = inorder.index(postorder.pop())
            node = TreeNode(inorder[index])
            node.left = self.buildTree(inorder[:index],postorder[:index])
            node.right = self.buildTree(inorder[index+1:],postorder[index:])
            return node
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
    head = s.buildTree([9,3,15,20,7],[9,15,7,20,3])
    s.print_tree(head)