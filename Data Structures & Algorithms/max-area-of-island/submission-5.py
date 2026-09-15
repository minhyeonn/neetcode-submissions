class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(-1,0),(0,-1), (0,1), (1,0)]
        def dfs(r,c):
            if not (0<=r<len(grid)) or not (0<=c<len(grid[0])) or grid[r][c]==0:
                return 0
            grid[r][c]=0


            return (1+dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    res = max(res, dfs(r,c))  
        return res           