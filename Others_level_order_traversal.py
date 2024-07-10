class Node:
    '''
    Structure of Node with mulitple children
    '''
    def __init__(self, val=0, children = []):
        self.val = val
        self.child = children


class Solution():
    def Level_Inorder(self,root):
        size_que = 1 #size of the queue that would let you know the number of nodes in a level
        level_ele = [root] #queue used for all the elements in the level
        final_ans = [] #to store the final ans in list<list> format
        level_order_ans = [] #to store the intermediate values in an array that will be appended in the fianl ans later

        while size_que != 0: #if the size of the queue is zero then the process will stop
            curr_node = level_ele.pop(0) #to pop the element so that the next level nodes can be added to the queue
            size_que -= 1 #to update the size of the queue
            level_order_ans.append(curr_node.val) #to append current node in the intermediate list so that once all the elements are over from the level, it can be added to the fianl ans
            for i in curr_node.child: #put all the children in the queue
                level_ele.append(i)
            if size_que == 0: #to check if all the elements in the level are visited with the use of size
                final_ans.append(level_order_ans.copy()) #if size is zero means that all the elements from that level are visited
                level_order_ans.clear() #to clear the intermediate value array so that new level nodes can be stored
                size_que = len(level_ele) #to update the value of queue. Since all the nodes are visited means all the next level nodes are added to the queue.
        print(final_ans)

if __name__ == "__main__":
    s = Solution()

    node8 = Node(8)
    node7 = Node(7)
    node6 = Node(6)
    node5 = Node(5)
    node4 = Node(4)
    node3 = Node(3, [node4, node5])
    node2 = Node(2,[node6, node7,node8])
    node1 = Node(1, [node2, node3])
    s.Level_Inorder(node1)