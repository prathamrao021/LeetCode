# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next



    def sortList(self, head):
        if head == None: return None
        if head.next != None:
            slow = head
            fast = head

            while fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
            
            second_head = slow.next
            slow.next = None

            left = self.sortList(head)
            right = self.sortList(second_head)

            head = self.mergeTwoLists(left,right)
            return head
        else:
            return head
    
    def print_list(self,root):
        while root != None:
            print(root.val,end="->")
            root = root.next

if __name__ == "__main__":
    s = Solution()
    l3 = ListNode(3)
    l1 = ListNode(1, l3)
    l2 = ListNode(2, l1)
    l4 = ListNode(4, l2)
    s.print_list(l4)

    head = s.sortList(l4)
    s.print_list(head)
