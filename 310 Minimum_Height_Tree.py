import collections
# class Solution:
#     def make_root(self, stack, count, node):
#         height = count
#         if height > self.min_h:
#             return float('inf')
#         for j in self.graph[node]:
#             if j not in stack:
#                 height = max(height,self.make_root(stack+[j],count+1, j))
#         return height
#     def findMinHeightTrees(self, n: int, edges):
#         if n == 1: return ([0])
#         if n == 0: return None
#         self.graph = collections.defaultdict(list)
#         def make_graph():
#             for i in range(len(edges)):
#                 self.graph[edges[i][0]].append(edges[i][1])
#                 self.graph[edges[i][1]].append(edges[i][0])
#         make_graph()
#         self.graph = sorted(self.graph.items, key = lambda item: len(item[1]), reverse=True)
#         print(self.graph)

#         stack = []
#         count = 0
#         self.min_h = float('inf')
#         ans= []
#         for i in self.graph.keys():
#             # min_h = min(min_h, self.make_root(stack+[i], count, i))
#             curr_h = self.make_root(stack+[i], count, i)
#             if self.min_h > curr_h:
#                 ans.clear()
#                 ans.append(i)
#                 self.min_h = curr_h
#             elif self.min_h == curr_h:
#                 ans.append(i)
#         return(ans)

class Solution:
    def findMinHeightTrees(self, n: int, edges):
        self.graph = collections.defaultdict(list)
        def make_graph():
            for i in range(len(edges)):
                self.graph[edges[i][0]].append(edges[i][1])
                self.graph[edges[i][1]].append(edges[i][0])
        make_graph()
        print(self.graph)
        while len(self.graph) != 2 and len(self.graph) != 1:
        
            prev_leaves = []
            for i in self.graph.keys():
                if len(self.graph[i]) == 1:
                    prev_leaves.append(i)
            
            for i in prev_leaves:
                self.graph[self.graph[i][0]].remove(i)
                del self.graph[i]
            print(self.graph)
        return list(self.graph.keys())
if __name__ == "__main__":
    s = Solution()
    k = s.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]])
    print(k)