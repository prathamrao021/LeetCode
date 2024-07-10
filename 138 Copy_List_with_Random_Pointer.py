class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        old_to_new = {}
        
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        print(old_to_new)
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new[curr.next]
            old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]

if __name__ == "__main__":
    s = Solution()
    n1 = Node(1)
    n11 = None
    n10 = Node(10,n1,n11)
    n11 = Node(11,n10)
    n7 = None
    n13 = Node(13,n11,n7)
    n7 = Node(7,n13)
    s.copyRandomList(n7)