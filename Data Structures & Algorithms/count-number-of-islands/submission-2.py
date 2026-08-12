class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        dir = [(-1,0), (0,-1), (1,0), (0,1)]

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dx, dy in dir:
                    nx = dx+row
                    ny = dy+col
                    if (0<= nx < rows) and (0 <= ny < cols) and grid[nx][ny]=="1":
                        grid[nx][ny]="0"
                        q.append((nx, ny))
                        bfs(nx, ny)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
        return islands

