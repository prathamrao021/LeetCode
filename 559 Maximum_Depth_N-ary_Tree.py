class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def tree_traversal(self,node, curr_depth, all_children):
        all_children= []
        if node.children != None:
            for child in node.children:
                all_children.append(self.tree_traversal(child, curr_depth, all_children))
            curr_depth = max(all_children)
        curr_depth += 1
        return curr_depth


    def maxDepth(self, root) -> int:
        max_depth = 1
        if root == None: return 0
        max_depth = self.tree_traversal(root, 0, [])
        return max_depth
    
if __name__ == "__main__":
    s = Solution()
    n5 = Node(5)
    n6 = Node(6)
    n3 = Node(3, [n5,n6])
    n2 = Node(2)
    n4 = Node(4)
    n1 = Node(1,[n3,n2,n4])

    print(s.maxDepth(n1))