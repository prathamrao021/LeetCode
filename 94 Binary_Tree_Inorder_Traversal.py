class Solution:
    def get_print_inordertraverse(self, root, final):
        if root == None:
            return
        self.get_print_inordertraverse(root.left, final)
        final.append(root.val)
        self.get_print_inordertraverse(root.right, final)
    def inorderTraversal(self, root):
        final = []
        self.get_print_inordertraverse(root, final)
        return final