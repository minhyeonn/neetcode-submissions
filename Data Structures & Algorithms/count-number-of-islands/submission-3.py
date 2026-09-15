class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        islands = 0

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        def dfs(r,c):
            if not (0<=r<len(grid)) and (0<=c<len(grid[0])):
                return
            for d1, d2 in directions:
                row = d1 + r
                col = d2 + c
                if 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]=='1':
                    grid[row][col]='0'
                    dfs(row,col)

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    dfs(r,c)
                    islands+=1
        return islands
