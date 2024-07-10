import collections
class Solution(object):
    def dfs(self,adjacency_matrix,curr_c):
        self.visited.add(curr_c)
        self.node_stack.append(curr_c)
        
        if adjacency_matrix.get(curr_c):
            for nei in adjacency_matrix.get(curr_c):
                if nei not in self.visited:
                    self.dfs(adjacency_matrix,nei)
                elif nei in self.node_stack:
                    self.is_cycle = True
                    return
        
        self.node_stack.pop()
        return
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjacency_matrix = collections.defaultdict(set)
        self.is_cycle = False
        self.visited = set()
        self.node_stack = []
        for i in range(len(prerequisites)):
            adjacency_matrix[prerequisites[i][0]].add(prerequisites[i][1])

        # print(adjacency_matrix)

        for node in adjacency_matrix.keys():
            if node not in self.visited:
                self.dfs(adjacency_matrix,node)
        
        return (not self.is_cycle)

if __name__ == "__main__":
    s = Solution()
    k = s.canFinish(3, [[0,1],[0,2],[1,2]])
    print(k)
