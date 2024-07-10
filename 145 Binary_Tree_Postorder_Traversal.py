# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def get_list_post(self, node, ans):
        if node == None:
            return ans
        
        ans = self.get_list_post(node.left,ans)
        ans = self.get_list_post(node.right, ans)
        ans.append(node.val)

        return ans

    def postorderTraversal(self, root):
        if root == None:
            return ([])
        ans = []
        ans = self.get_list_post(root,ans)
        return ans


if __name__ == "__main__":
    s = Solution()
    t3 = TreeNode(3)
    t2 = TreeNode(2,t3)
    t1 = TreeNode(1, None, t2)
    k = s.postorderTraversal(t1)
    print(k)