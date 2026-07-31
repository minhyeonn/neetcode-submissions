from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q = deque()
                    q.append((i,j))
                    while q:

                        r,c = q.popleft()
                        for drow, dcol in directions:
                            if r+drow<0 or r+drow>=len(grid) or c+dcol <0 or c+dcol>=len(grid[0]) or grid[r+drow][c+dcol]==-1:
                                continue

                            if grid[r+drow][c+dcol]>grid[r][c]+1:
                                grid[r+drow][c+dcol] = grid[r][c]+1
                                q.append((r+drow, c+dcol))
