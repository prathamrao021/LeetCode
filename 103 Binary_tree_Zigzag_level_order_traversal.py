class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if root == None: 
            return []
        temp_ans = []
        final_ans = []
        queue = [root]
        size = 1
        left_to_right = True
        while len(queue) != 0:
            if size == 0:
                size = len(queue)
                if left_to_right:
                    final_ans.append(temp_ans)
                    left_to_right = False
                else:
                    temp_ans.reverse()
                    final_ans.append(temp_ans)
                    left_to_right = True
                temp_ans = []
            elif size != 0:
                new_node = queue.pop(0)
                temp_ans.append(new_node.val)
                size -= 1
                if new_node.left != None:
                    queue.append(new_node.left)
                if new_node.right != None:
                    queue.append(new_node.right)
        if left_to_right:
            final_ans.append(temp_ans)
        else:
            temp_ans.reverse()
            final_ans.append(temp_ans)
        return final_ans

# node6 = Node(6, None, None)
# node2 = Node(2, None, None)
# node1 = Node(1, None, None)
# node3 = Node(3, node1, node2)
# node5 = Node(5, node6, None)
# node4 = Node(4, node3, node5)
    

node3 = Node(3, None, None)
node2 = Node(2, None, None)
node1 = Node(1, node2, node3)
s = Solution()
k = s.zigzagLevelOrder(node1)
print(k)