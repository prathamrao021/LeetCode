# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head == None: 
            return False
        double_jump = head.next
        if double_jump == None: return False
        single_jump = head
        cycle_flag = False
        while single_jump != None:
            if double_jump == single_jump:
                cycle_flag = True
                break
            if double_jump.next != None:
                if double_jump.next.next != None:
                    double_jump = double_jump.next.next
                else: break
            else: break
            single_jump = single_jump.next
        return cycle_flag