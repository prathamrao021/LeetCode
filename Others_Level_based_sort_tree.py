class Node:
    def __init__(self, val=None, leftchild=None, rightchild=None):
        self.val = val
        self.left = leftchild
        self.right = rightchild

class Solution:
    def sort_by_level(self, root):
        if root == None:
            return
        final = []
        queue = [root]
        temp = []
        size = 1
        while queue:
            # node = queue.pop(0)
            # final.append(node.val)
            # if node.left != None:
            #     queue.append(node.left)
            # if node.right != None:
            #     queue.append(node.right)
            if size == 0:
                final.append(temp)
                temp = []
                size = len(queue)
                continue
            elif size != 0:
                v = queue.pop(0)
                size -= 1
                if v.left != None:
                    queue.append(v.left)
                if v.right != None:
                    queue.append(v.right)
                temp.append(v.val)
        final.append(temp)
        return final
    
if __name__ == "__main__":
    
    node4 = Node(4, None, None)
    node5 = Node(5, None, None)
    node6 = Node(6, None, None)
    node7 = Node(7, None, None)
    node3 = Node(3, node6, node7)
    node2 = Node(2, node4, node5)
    node1 = Node(1, node2, node3)

    s = Solution()
    print(s.sort_by_level(node1))