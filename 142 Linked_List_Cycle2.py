# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

# class Solution:
#     def detectCycle(self, head):
#         visited_nodes = set()
#         dummy = head
#         while dummy != None:
#             if dummy in visited_nodes:
#                 return dummy
#             visited_nodes.add(dummy)
#             dummy = dummy.next
#         return None


class Solution:
    def detectCycle(self, head):
        count_slow = 0
        count_fast = 0
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        if fast == None or fast.next == None:
            return None

if __name__ == "__main__":
    s = Solution()

    n4 = ListNode(-4)
    n0 = ListNode(0,n4)
    n2 = ListNode(2,n0)
    n3 = ListNode(3,n2)
    n4.next = n2    

    print(s.detectCycle(n3).val) # 2