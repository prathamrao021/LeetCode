class Node:
    def __init__(self, val=None, leftchild=None, rightchild=None):
        self.val = val
        self.left = leftchild
        self.right = rightchild
class Solution:
    def in_order_traversal_stack(self, root):
        ans = []
        stack_pre = []
        curr = root
        while curr != None or len(stack_pre) != 0:
            while curr != None:
                stack_pre.append(curr)
                curr = curr.left
            curr = stack_pre.pop()
            ans.append(curr.val)
            curr = curr.right

        print(ans)
    
node6 = Node(6, None, None)
node2 = Node(2, None, None)
node1 = Node(1, None, None)
node3 = Node(3, node1, node2)
node5 = Node(5, node6, None)
node4 = Node(4, node3, node5)
s = Solution()
s.in_order_traversal_stack(node4)
