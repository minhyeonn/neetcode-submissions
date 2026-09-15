class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        q = deque()
        visit = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    visit.add((r,c))
                    q.append((r,c))

        def bfs(r,c):
            if not 0<=r<len(grid) or not 0<=c<len(grid[0]) or (r,c) in visit or grid[r][c]==-1:
                return
            visit.add((r,c))
            q.append((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r+1, c)
                bfs(r-1, c)
                bfs(r, c+1)
                bfs(r, c-1)
            dist+=1
            



