# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None: 
            return head
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            # print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next

        first_list_end = slow
        sec_list_start = slow.next

        node = sec_list_start
        next_node = sec_list_start.next
        prev_node = None

        while node != None:
            node.next = prev_node
            prev_node = node
            node = next_node
            if next_node != None:
                next_node = next_node.next



        first_list_end.next = None
        sec_list_start = prev_node
        next_sec = prev_node.next
        next_fir = head.next
        node = head
        while node != None:
            node.next = sec_list_start
            if sec_list_start != None:
                sec_list_start.next = next_fir
            node = next_fir
            if next_fir != None:
                next_fir = next_fir.next
            sec_list_start = next_sec
            if next_sec != None:
                next_sec = next_sec.next
        #node.next = None

        dummy = head
        while dummy != None:
            print(dummy.val, end=">")
            dummy = dummy.next

if __name__ == "__main__":
    s = Solution()
    # l5 = ListNode(5)
    l4 = ListNode(4)
    l3 = ListNode(3,l4)
    l2 = ListNode(2,l3)
    l1 = ListNode(1,l2)
    s.reorderList(l1)

        
        