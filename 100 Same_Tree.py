# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check_same(self,tree1,tree2,check):
        if check == False:
            return check
        if tree1.left != None and tree2.left != None:
            check = self.check_same(tree1.left, tree2.left, check)
        elif (tree1.left != None and tree2.left == None) or (tree1.left == None and tree2.left != None):
            check = False
        if tree1.val != tree2.val:
            check = False
        if tree1.right != None and tree2.right != None:
            check = self.check_same(tree1.right, tree2.right, check)
        elif (tree1.right != None and tree2.right == None) or (tree1.right == None and tree2.right != None):
            check = False
        return check
    
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
            
        check = True
        check = self.check_same(p,q, check)
        return check

node21 = Node(2, None, None)
node31 = Node(4, None, None)
node11 = Node(1, node21, node31)

node22 = Node(2, None, None)
node32 = Node(3, None, None)
node12 = Node(1, node22, node32)

s = Solution()
k = s.isSameTree(node11,node12)
print(k)