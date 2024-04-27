import  sys
class Node:
    def __init__(self, val=None, leftchild=None, rightchild=None):
        self.val = val
        self.left = leftchild
        self.right = rightchild

class Solution:   
    def __init__(self):
        self.dummy = Node()
        self.final = []

    def in_order_traversal(self, root):
        if root == None:
            return
        self.in_order_traversal(root.left)
        self.final.append(root.val)
        self.in_order_traversal(root.right)
        # print("gets here")
        return self.final
    
    # tried this interatively but failed

    # def in_order_traversal(self, root):
    #     final = []
    #     dummy = Node()
    #     dummy = root
    #     while True:
    #         if dummy.leftchild != None:
    #             dummy = root.leftchild
    #         elif dummy.leftchild == None:
    #             final.append(dummy.val)

    #         if dummy.rightchild != None:s
    #             dummy = dummy.rightchild
    #         elif dummy.rightchild == None:
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

                
node6 = Node(6, None, None)
node2 = Node(2, None, None)
node1 = Node(1, None, None)
node3 = Node(3, node1, node2)
node5 = Node(5, node6, None)
node4 = Node(4, node3, node5)
s = Solution()
s.in_order_traversal(node4)
print(s.final)