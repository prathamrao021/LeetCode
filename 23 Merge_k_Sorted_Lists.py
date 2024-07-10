import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if lists == None or len(lists) == 0:
            return (None)
        if len(lists) == 1:
            return lists[0]
        queue = collections.deque(lists)

        while len(queue) != 1:
            list1 = queue.popleft()
            list2 = queue.popleft()
            temp = ListNode()
            head = temp
            while list1 != None and list2 != None:
                if list1.val == list2.val:
                    list1_next = list1.next
                    list2_next = list2.next
                    temp.next = list1
                    list1.next = list2
                    list2 = list2_next
                    list1 = list1_next
                    temp = temp.next.next 
                    

                elif list1.val > list2.val:
                    temp.next = list2
                    list2 = list2.next
                    temp = temp.next
                elif list1.val < list2.val:
                    temp.next = list1
                    list1 = list1.next
                    temp = temp.next
            if list2 == None:
                while list1 != None:
                    temp.next = list1
                    list1 = list1.next
                    temp = temp.next
            if list1 == None:
                while list2 != None:
                    temp.next = list2
                    list2 = list2.next
                    temp = temp.next    
            queue.append(head.next)   
        return head.next

if __name__ == "__main__":
    s = Solution()

    l5 = ListNode(5)
    l4 = ListNode(4,l5)
    l1 = ListNode(1,l4)

    l4_1 = ListNode(4)
    l3 = ListNode(3,l4_1)
    l1_1 = ListNode(1,l3)

    l6 = ListNode(6)
    l2 = ListNode(2,l6)
    l0 = ListNode(0,l2)
    l_n4 = ListNode(-4,l0)


    s.mergeKLists([l1,l1_1,l_n4])