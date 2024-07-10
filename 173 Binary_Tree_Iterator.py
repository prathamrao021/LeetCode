# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder_calculate(self,node):
        if node == None: return

        self.inorder_calculate(node.left)
        self.inorder_list.append(node.val)
        self.inorder_calculate(node.right)

    def __init__(self, root):
        self.inorder_list = []
        self.inorder_calculate(root)
        self.curr_val = -1

    def next(self) -> int:
        self.curr_val += 1
        return self.inorder_list[self.curr_val]

    def hasNext(self) -> bool:
        # print(self.curr_val)
        if self.curr_val+1 < len(self.inorder_list):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()