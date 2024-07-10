# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        new_head = head
        node = head.next
        # curr_node = head
        prev_node = head
        next_node = head.next.next
        while node != None:
            curr_node = new_head
            sub_prev_node =  None

            while curr_node != node:
                if node.val < curr_node.val:
                    if curr_node == new_head:
                        new_head = node
                    if sub_prev_node != None:
                        sub_prev_node.next = node
                    node.next = curr_node
                    prev_node.next = next_node
                    break
                sub_prev_node = curr_node
                curr_node = curr_node.next
            
            
            if prev_node.next == node:
                prev_node = node
            node = next_node
            if next_node != None:
                next_node = next_node.next
        
        return new_head


if __name__ == "__main__":
    s = Solution()
    l3 = ListNode(3)
    l1 = ListNode(1,l3)
    l2 = ListNode(2,l1)
    l4 = ListNode(4,l2)
    s.insertionSortList(l4) 
