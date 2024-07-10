# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root):
        queue_size = 1
        general_queue = [root]
        level_nodes = []
        ans = []
        while queue_size != 0:
            curr_node = general_queue.pop(0)
            queue_size -= 1
            level_nodes.append(curr_node.val)
            if curr_node.left != None:
                general_queue.append(curr_node.left)
            if curr_node.right != None:
                general_queue.append(curr_node.right)
            if queue_size == 0:
                ans.append(level_nodes.copy())
                level_nodes.clear()
                queue_size = len(general_queue)
        ans.reverse()
        return(ans)
            
if __name__ == "__main__":
    s = Solution()
    n5 = TreeNode(15)
    n4 = TreeNode(7)
    n3 = TreeNode(20,n5,n4)
    n2 = TreeNode (9)
    n1 = TreeNode(3,n2,n3)
    s.levelOrderBottom(n1)
        