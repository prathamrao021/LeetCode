# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA,headB):
        if headA == headB:
            return headA
        arr1 = []
        arr2 = []
        dum1 = headA
        dum2 = headB
        found_inter = False
        while dum1 != None:
            arr1.append(dum1)
            dum1 = dum1.next

        while dum2 != None:
            arr2.append(dum2)
            dum2 = dum2.next

        print(arr1,arr2)

        for i in range(-1,-(min(len(arr2),len(arr1)))-1,-1):
            if arr1[i] != arr2[i]:
                if i == -1:
                    return None
                found_inter = True
                ans = arr1[i].val
                break
        if not found_inter:
            return None
        return(arr1[i+1])






if __name__ == "__main__":
    s = Solution()
    # n5 = ListNode(5)
    # n4_1 = ListNode(4,n5)
    # n8 = ListNode(8,n4_1)
    # n1 = ListNode(1,n8)
    # n4 = ListNode(4,n1)


    # n1_1 = ListNode(1,n8)
    # n6 = ListNode(6,n1_1)
    # n5_1 = ListNode(5,n6)


    # n4 = ListNode(4)
    # n2 = ListNode(2,n4)
    # n1 = ListNode(1,n2)
    # n9 = ListNode(9,n1)
    # n1_1 = ListNode(1,n9)

    # n3 = ListNode(3,n2)



    n4 = ListNode(4)
    n6 = ListNode(6,n4)
    n2 = ListNode(2,n6)

    n5 = ListNode(5)
    n1 = ListNode(1,n5)


    k = s.getIntersectionNode(n1,n2)
    print(k.val)


    