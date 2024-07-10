import sys
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root == None:
            return None
        queue_size = 1
        node_queue = [root]
        # level = 1
        while queue_size != 0:
            curr_node = node_queue.pop(0)
            queue_size -= 1
            if  queue_size == 0:
                curr_node.next = None
            else:
                curr_node.next = node_queue[0]
            
            if curr_node.left != None:
                node_queue.append(curr_node.left)
            if curr_node.right != None:
                node_queue.append(curr_node.right)
            
            if queue_size == 0:
                queue_size = len(node_queue)
        return root

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
    n6 = Node(6)
    n7 = Node(7)
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3,n6,n7)
    n2 = Node(2,n4,n5)
    n1 = Node(1,n2,n3)
    s.print_tree(n1)
    s.connect(n1)
    
        