import collections
class Solution:
    def bfs(self, image, q, color, already):
        max_row = len(image)-1
        max_col = len(image[0])-1
        if len(q)>0:
            x = q.popleft()
            r,c = x[0],x[1]
            if r > max_row or c > max_col or r < 0 or c < 0 or image[r][c]==color or image[r][c]!=already:
                return image
        
            image[r][c] = color
            q.append([r+1,c])
            q.append([r,c+1])
            q.append([r-1,c])
            q.append([r,c-1])

            image = self.bfs(image, q, color, already)
            return image
        else:
            return image
        
        
    
    
    def floodFill(self, image, sr: int, sc: int, color: int):
        q = collections.deque([[sr,sc]])
        already = image[sr][sc]
        while q:
            image = self.bfs(image, q, color, already)
    
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))