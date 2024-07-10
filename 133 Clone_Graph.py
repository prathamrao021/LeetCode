"""
# Definition for a Node."""
class Node:
    def __init__(self, val = 1, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        visit = set()
        queue = [node]
        dummy = node
        clone_dict = {}
        while len(queue)!= 0:
            curr_node = queue.pop(0)
            clone_dict[curr_node] = Node(curr_node.val)
            if (len(curr_node.neighbors) != 0):
                for i in curr_node.neighbors:
                    if i.val not in visit and i not in queue:
                        queue.append(i)
            visit.add(curr_node.val)
        
        for i in clone_dict:
            for j in i.neighbors:
                clone_dict[i].neighbors.append(clone_dict[j])
        
        print(visit)
        return (clone_dict[node])
    
if __name__ == "__main__":
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node4,node2]
    node2.neighbors = [node1,node3]
    node3.neighbors = [node2,node4]
    node4.neighbors = [node1,node3]
    s.cloneGraph(node1)