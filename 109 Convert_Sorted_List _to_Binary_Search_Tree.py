import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def calculate_child(self, head):
            if head == None: return None
            pre_node = ListNode(val= -(10**6))
            dummy_single = head
            dummy_double = head

            while dummy_double != None and dummy_double.next != None:
                dummy_double = dummy_double.next.next
                pre_node = dummy_single
                dummy_single = dummy_single.next
            
            # print(dummy_single.val, next_node.val)
            if pre_node.val != -(10**6):
                pre_node.next = None
            else:
                temp = TreeNode(dummy_single.val)
                return temp
            
            left_tree = self.calculate_child(head)
            right_tree = self.calculate_child(dummy_single.next)
            root = TreeNode(dummy_single.val,left_tree, right_tree)
            return root
    def sortedListToBST(self, head):
        root = TreeNode()
        root = self.calculate_child(head)
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
    l1 = ListNode(9)
    l2 = ListNode(5, l1)
    l3 = ListNode(0, l2)
    l4 = ListNode(-3, l3)
    l5 = ListNode(-10, l4)
    root = s.sortedListToBST(l5)
    s.print_tree(root)
    