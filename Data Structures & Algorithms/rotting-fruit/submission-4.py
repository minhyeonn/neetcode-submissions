from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        fresh = 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    if r+dr<0 or r+dr>=len(grid) or c+dc<0 or c+dc>=len(grid[0]) or grid[r+dr][c+dc]!=1:
                        continue
                    
                    q.append((r+dr, c+dc))
                    grid[r+dr][c+dc] = 2
                    fresh-=1
            res+=1
        return res if fresh ==0 else -1