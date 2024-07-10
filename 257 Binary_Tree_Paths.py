class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def calculate(self, node, inter_ans):
        if node.right == None and node.left == None:
            inter_ans += str(node.val)
            self.result.append(inter_ans)
            return
        # inter_ans = inter_ans+"->"+str(node.val)
        if node.right != None:
            self.calculate(node.right,inter_ans+str(node.val)+"->")
        if node.left != None:
            self.calculate(node.left,inter_ans+str(node.val)+"->")



    def binaryTreePaths(self, root):
        if root == None:
            return None
        self.result = []
        inter_ans = ""
        self.calculate(root,inter_ans)
        return(self.result)

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)

    t4 = TreeNode(4,t2,t1)
    t5 = TreeNode(5,None,t3)

    t6 = TreeNode(6,t4, t5)

    s.binaryTreePath(t6)