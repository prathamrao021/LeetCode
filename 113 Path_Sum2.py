
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recursive_nodecalling(self, node, target, final_ans, temp_ans):
        if target == 0:
            if node.right == None and node.left == None:
                final_ans.append(temp_ans.copy())
                return final_ans
            else:
                if node.left != None:
                    final_ans = self.recursive_nodecalling(node.left, target-node.left.val, final_ans, temp_ans+[node.left.val])
                if node.right != None:
                    final_ans = self.recursive_nodecalling(node.right, target-node.right.val, final_ans, temp_ans+[node.right.val])
                return final_ans
        if target != 0:
            if node.left != None:
                final_ans = self.recursive_nodecalling(node.left, target-node.left.val, final_ans, temp_ans+[node.left.val])
            if node.right != None:
                final_ans = self.recursive_nodecalling(node.right, target-node.right.val, final_ans, temp_ans+[node.right.val])
            return final_ans

    def pathSum(self, root, targetSum):
        if root == None:
            return []
        final_ans = []
        temp_ans = []
        if targetSum == root.val:
            if root.left == None and root.right == None:
                return ([[root.val]])
            else:
                final_ans = self.recursive_nodecalling(root,targetSum-root.val,final_ans,temp_ans+[root.val])
                return final_ans
        final_ans = self.recursive_nodecalling(root,targetSum-root.val,final_ans,temp_ans+[root.val])
        return final_ans
        
    
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
    # t1 = TreeNode(7)
    # t2 = TreeNode(2)
    # t3 = TreeNode(11,t1,t2)
    # t4 = TreeNode(5)
    # t5 = TreeNode(1)
    # t6 = TreeNode(4,t4,t5)
    # t7 = TreeNode(13)
    # t8 = TreeNode(8, t7, t6)
    # t9 = TreeNode(4,t3)
    # t10 = TreeNode(5,t9,t8)

    # t2 = TreeNode(-3)
    # t1 = TreeNode(-2,None,t2)
    
    
    t1 = TreeNode(-1)
    t2 = TreeNode(1,t1)
    t3 = TreeNode(3)
    t4 = TreeNode(-2,t2,t3)
    t5 = TreeNode(-2)
    t6 = TreeNode(-3,t5)
    t7 = TreeNode(1,t4,t6)

    
    s.print_tree(t7)
    k = s.pathSum(t7, -1)
    print(k)