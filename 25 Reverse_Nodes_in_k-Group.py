# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_be_done(self, node, k):
        k -= 1
        while k >= 0:
            if node == None:
                return False
            k -= 1
            node = node.next
        return True

    def reverseKGroup(self, head, k):
        new_head = ListNode()
        new_head.next = head

        prev_node = new_head
        # next_node = ListNode()
        count = 0
        front_prev = prev_node
        rear = head
        front = head
        front_next = head.next
        if front_next == None: return head
        # rear = ListNode()

        while front !=  None:
            if not self.reverse_be_done(front, k):
                break
            count = 0
            while front != None and count != k:
                front.next = front_prev
                front_prev = front
                front = front_next
                if front_next!= None:
                    front_next = front_next.next
                count += 1
            rear.next = front
            prev_node.next = front_prev
            prev_node = rear
            front_prev = prev_node
            # front = front_prev.next
            # front_next = front.next
            rear = front

        return new_head.next

    
    def print_list(self,head):
        while head != None:
            print(head.val,end="->")
            head = head.next

if __name__ == "__main__":
    s = Solution()
    
    l5 = ListNode(5)
    l4 = ListNode(4,l5)
    l3 = ListNode(3,l4)
    l2 = ListNode(2,l3)
    l1 = ListNode(1,l2)

    s.print_list(l1)
    head = s.reverseKGroup(l1,2)
    s.print_list(head)
