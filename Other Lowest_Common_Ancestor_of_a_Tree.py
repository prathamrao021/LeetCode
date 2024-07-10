import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    # def dfs(self,node,p,q, temp_stack):
    #     if node.val == p.val:
    #         self.parent_stack1 = temp_stack
    #     if node.val == q.val:
    #         self.parent_stack2 = temp_stack
        
    #     if node.left != None:
    #         self.dfs(node.left, p, q, temp_stack+[node.left])
    #     if node.right != None:
    #         self.dfs(node.right, p, q, temp_stack+[node.right])
    #     return 
    # def lowestCommonAncestor(self, root, p, q):
    #     if p == root or q == root:
    #         return root
    #     self.parent_stack1 = []
    #     self.parent_stack2 = []
    #     temp_stack = [root]
    #     self.dfs(root,p,q,temp_stack)

    #     result = TreeNode(0)
    #     for i in range(min(len(self.parent_stack1),len(self.parent_stack2))):
    #         if self.parent_stack1[i].val == self.parent_stack2[i].val:
    #             result = self.parent_stack1[i]
    #         else:
    #             break
    #     return result

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r

    def print_tree(self, node, indent="", last='updown'):
        nb_space = 10
        if node != None:
            sys.stdout.write(indent)
            if last == 'updown':
                sys.stdout.write('----')
                indent += "     "
            elif last == 'leftright':
                sys.stdout.write(' /-- ')
                indent += "|    "
            else:
                sys.stdout.write(' \\-- ')
                indent += '     ' 
        print(str(node.val))
        if node.left is not None:
            self.print_tree(node.left, indent, 'leftright')
        if node.right is not None:
            self.print_tree(node.right, indent, 'updown')

if __name__ == "__main__":
    s = Solution()
    t3 = TreeNode(3)
    t5 = TreeNode(5)
    t4 = TreeNode(4,t3,t5)
    t0 = TreeNode(0)
    t2 = TreeNode(2,t0,t4)
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t8 = TreeNode(8,t7, t9)
    t6 = TreeNode(6,t2,t8)
    
    s.print_tree(t6)
    k = s.lowestCommonAncestor(t6,t4,t5)
    print(k.val)
