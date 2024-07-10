# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val: int):
        dummy = head
        new_head = head
        while dummy != None and dummy.val == val:
            dummy = dummy.next
        new_head = dummy
        if new_head == None:
            return new_head
        # print(new_head.val)

        rem = new_head
        pre_nod = ListNode()

        while rem != None:
            if rem.val == val:
                pre_nod.next = rem.next
                rem = rem.next
                continue
            pre_nod = rem
            rem = rem.next
        return new_head

if __name__ == "__main__":
    s = Solution()
    l6 = ListNode(6)
    l5 = ListNode(5,l6)
    l4 = ListNode(4,l5)
    l3 = ListNode(3,l4)
    l2 = ListNode(2,l3)
    l1 = ListNode(1,l2)

    s.removeElements(l1,2)