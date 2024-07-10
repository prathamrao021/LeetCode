# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        avg_arr = []
        queue = [root]
        count = 1
        divi = 1
        add  = 0
        while count:
            curr_node = queue.pop(0)
            count -= 1
            add += curr_node.val
            if curr_node.left != None:
                queue.append(curr_node.left)
            if curr_node.right != None:
                queue.append(curr_node.right)
            
            if count == 0:
                avg_arr.append(float(add/divi))
                add = 0
                divi = len(queue)
                count = len(queue)

        return avg_arr

if  __name__ == "__main__":
    s = Solution()
    
    t15 = TreeNode(15)
    t7 = TreeNode(7)
    t9 = TreeNode(9)
    t20 = TreeNode(20,t15,t7)
    t3 = TreeNode(3,t9,t20)

    k = s.averageOfLevels(t3)
    print(k)