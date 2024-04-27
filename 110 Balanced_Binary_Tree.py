# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def assign_weights(self, node, check):
        if check == False:
            return (0,False)
        if node == None:
            return 0,True
        h_left,check = self.assign_weights(node.left,check)
        h_right,check = self.assign_weights(node.right,check)
        
        if check == False:
            return (0,False)
        
        if(abs(h_left-h_right)<=1):
            check = True
        else:
            check = False
            return (0,check)
        
        return (max(h_left,h_right)+1,check)
    
    def isBalanced(self, root):
        if root == None:
            return True
        check = True
        x,check = self.assign_weights(root, check)
        print(x,check)

s = Solution()
# node6 = TreeNode(6)
# node8 = TreeNode(8)
# noden1 = TreeNode(-1, None, node8)
# node3 = TreeNode(3,None,node6)
# node1_1 = TreeNode(1)
# node5 = TreeNode(5)
# node1 = TreeNode(1, node5, node1_1)
# node4 = TreeNode(4, node3, noden1)
# node2 = TreeNode(2, node1)
# node0 = TreeNode(0, node2, node4)

node5 = TreeNode(5)
node4 = TreeNode(4, node5)
node3 = TreeNode(3, node4)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, node2)
# node0 = TreeNode(0, node1)
s.isBalanced(node1)