# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        if root == None:
            return None
        ans = [root.val]
        queue = [root]
        size_q = 1
        i = 1
        while queue:
            curr_node = queue.pop(0)
            size_q -= 1
            if curr_node.left:
                queue.append(curr_node.left)
                if i <= len(ans)-1:
                    ans[i] = curr_node.left.val
                else:
                    ans.append(curr_node.left.val)
            if curr_node.right:
                queue.append(curr_node.right)
                if i <= len(ans)-1:
                    ans[i] = curr_node.right.val
                else:
                    ans.append(curr_node.right.val)
            if size_q == 0:
                i+=1
                size_q = len(queue)
        return(ans)


if __name__ == "__main__":
    s = Solution()
    t6 = TreeNode(6)
    t4 = TreeNode(4,t6)
    t5 = TreeNode(5)
    t3 = TreeNode(3,t4,t5)
    t2 = TreeNode(2)
    t1 = TreeNode(1,t3,t2)

    s.rightSideView(t1)