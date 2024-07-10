class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prev_node = None
        node = head
        next_node = head.next

        while node != None:
            node.next = prev_node
            prev_node = node
            node = next_node
            if next_node != None:
                next_node = next_node.next
        return prev_node
    
    def print_list(self, node):
        while node != None:
            print(node.val, end=">")
            node = node.next

if __name__ == "__main__":
    s = Solution()
    l6 = ListNode(6)
    l5 = ListNode(5,l6)
    l4 = ListNode(4,l5)
    l3 = ListNode(3,l4)
    l2 = ListNode(2,l3)
    l1 = ListNode(1,l2)
    s.print_list(l1)
    head = s.reverseList(l1)
    s.print_list(head)
