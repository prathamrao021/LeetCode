import sys
class Node:
    def __init__(self, val=None, leftchild=None, rightchild=None):
        self.val = val
        self.left = leftchild
        self.right = rightchild
class Solution:
    def in_order_traversal_stack(self, root):
        if root == None:
            return ([])
        if root.left == None and root.right == None:
            return([root.val])
        traversing_stack = []
        ans = []
        last_node_to_be_reached = root
        while True:
            if last_node_to_be_reached.right != None:
                last_node_to_be_reached = last_node_to_be_reached.right 
            else:
                break
        dummy = root
        while dummy.val != last_node_to_be_reached.val or (last_node_to_be_reached.left != None and last_node_to_be_reached.left.val not in ans):
            if dummy.left != None and dummy.left.val not in ans:
                traversing_stack.append(dummy)
                dummy = dummy.left
            elif (dummy.left != None and dummy.left.val in ans)or(dummy.left == None):
                if dummy.val not in ans:
                    ans.append(dummy.val)
                if (dummy.right != None and dummy.right.val in ans)or(dummy.right == None):
                    dummy = traversing_stack.pop()
                elif dummy.right != None and dummy.right.val not in ans:
                    traversing_stack.append(dummy)
                    dummy = dummy.right
        ans.append(last_node_to_be_reached.val)
        # print(ans)
        return ans

    def print_tree(self, node, indent="", last='updown'):
        ''' 
            /--  = leftnode
            ---- = rightnode
            '   ' = children
        '''
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
node5 = Node(5, None, node6)
node4 = Node(4, node3, node5)
s = Solution()
s.print_tree(node4)
print(s.in_order_traversal_stack(node4))
