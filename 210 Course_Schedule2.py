# import collections
# class Solution:
#     def dfs(self, curr_ele):
#         self.visited.add(curr_ele)
#         self.loop_stack.append(curr_ele)

#         if self.grid.get(curr_ele) != None:
#             for i in self.grid[curr_ele]:
#                 if i not in self.visited:
#                     self.dfs(i)
#                 elif i in self.loop_stack:
#                     self.is_cycle = True
#                     return
#         self.loop_stack.pop()
#         return
#     def findOrder(self, numCourses, prerequisites):
#         self.grid = collections.defaultdict(set)
#         self.visited = set()
#         self.loop_stack = []
#         self.is_cycle = False

#         for i in range(len(prerequisites)):
#             self.grid[prerequisites[i][0]].add(prerequisites[i][1])
        
#         for i in range(numCourses):
#             if self.grid.get(i) == None:
#                 self.grid[i] = {}
        
#         for i in self.grid.keys():
#             if i not in self.visited:
#                 self.dfs(i)
#         if self.is_cycle:
#             return([])
#         all_nodes = set([i for i in range(numCourses)])
#         check_nodes = set()
#         ans = []
#         temp = []
#         while all_nodes != check_nodes:
#             for i in self.grid.keys():
#                 if i in check_nodes:
#                     continue
#                 if len(ans) == 0 and len(self.grid[i]) == 0:
#                     ans.append(i)
#                     check_nodes.add(i)
#                 else:
#                     x = self.grid[i]
#                     if len(x) == 0 or x.issubset(set(ans)):
#                         ans.append(i)
#                         check_nodes.add(i)
#         return(ans)
                

import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            return ([i for i in range(numCourses)])
        self.preq = collections.defaultdict(set)
        self.graph = collections.defaultdict(set)

        for i in range(len(prerequisites)):
            self.preq[prerequisites[i][0]].add(prerequisites[i][1])
            if self.preq[prerequisites[i][1]] == None:
                self.preq[prerequisites[i][1]] = {}
            self.graph[prerequisites[i][1]].add(prerequisites[i][0])
            if self.graph[prerequisites[i][0]] == None:
                self.preq[prerequisites[i][0]] = {}
        
        for i in range(numCourses):
            if self.preq[i] is None:
                self.preq[i] = {}
            if self.graph[i] is None:
                self.graph[i] = {}
        # print(self.preq, self.graph)
        ans = []
        q = collections.deque([])

        for k,v in self.preq.items():
            if len(v) == 0:
                q.append(k)
        

        while q:
            curr_c = q.popleft()
            ans.append(curr_c)

            if len(ans) == numCourses: return ans

            for nei in self.graph[curr_c]:
                self.preq[nei].remove(curr_c)
                if not self.preq[nei]:
                    q.append(nei)
                
        return ([])

if __name__ == "__main__":
    s = Solution()
    k = s.findOrder(3,[[1,0]])
    print(k)