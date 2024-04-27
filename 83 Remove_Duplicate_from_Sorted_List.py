# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def iterate(self, head, node):
        prev = head
        while node != None:
            if node.val == prev.val:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
        return head
    def deleteDuplicates(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        else:
            head = self.iterate(head, head.next)
        return head
    def print_list(self, head):
        node = head
        print("")
        while node != None:
            print(node.val, end=">")
            node = node.next
if __name__ == "__main__":
    s = Solution()
    node2 = ListNode(2)
    node11 = ListNode(1,node2)
    node1 = ListNode(1,node11)
    s.print_list(node1)
    head = s.deleteDuplicates(node1)
    # print(head.val)
    s.print_list(head)
    