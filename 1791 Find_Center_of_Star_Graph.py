class Solution:
    def findCenter(self, edges) -> int:
        connected_count = dict()

        for edge in edges:
            if connected_count.get(edge[0]) == None:
                connected_count[edge[0]]=1
            else:
                connected_count[edge[0]]+=1
            
            if connected_count.get(edge[1]) == None:
                connected_count[edge[1]]=1
            else:
                connected_count[edge[1]]+=1

        for key,val in connected_count.items():
            if val == len(edges):
                return key