class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visit = set()
        def dfs(i, j, visit):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i,j) in visit or grid[i][j] == 0:
                return 0
            visit.add((i,j))
            return 1 + dfs(i+1,j, visit) + dfs(i, j+1, visit) + dfs(i-1,j, visit) + dfs(i,j-1, visit)
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visit:
                    res = max(res, dfs(i,j,visit))
        return res