# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=-501, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        if left == 1:
            rev_start = head
            before_rev = None
        else:
            dum = head.next
            position = 2
            before_rev = head

            while dum != None:
                if position == left:
                    rev_start = dum
                    break
                before_rev = before_rev.next
                dum = dum.next
                position += 1

        after_rev = head
        
        
        dum = head
        position = 1
        
        while dum != None:
            if position == right:
                rev_end = dum
                after_rev = dum.next
                break
            dum = dum.next
            position += 1

        if rev_start.next == rev_end:
            if before_rev != None:
                before_rev.next = rev_end
            rev_end.next = rev_start
            rev_start.next = after_rev
        else:
            fir_rev = rev_start.next.next
            sec_rev = rev_start.next
            thr_rev = rev_start

            while sec_rev != after_rev:
                sec_rev.next = thr_rev
                thr_rev = sec_rev
                sec_rev = fir_rev
                if sec_rev == None:
                    break
                fir_rev = fir_rev.next

            rev_start.next = after_rev
        if left == 1:
            return rev_end
        else:
            before_rev.next = rev_end
            return head
    
    
    def print_list(self, head):
        node = head
        print("")
        while node != None:
            print(node.val, end=">")
            node = node.next

if __name__ == "__main__":
    s = Solution()
    # node5 = ListNode(5)
    # node4 = ListNode(4, node5)
    # node3 = ListNode(3, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(1, node2)
    # s.print_list(node1)
    # head = s.reverseBetween(node1, 2 ,4)
    # s.print_list(head)


    # node5 = ListNode(5)
    # node3 = ListNode(3, node5)
    # s.print_list(node3)
    # head = s.reverseBetween(node3, 1 ,2)
    # s.print_list(head)

    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    s.print_list(node1)
    head = s.reverseBetween(node1, 1 ,2)
    s.print_list(head)
