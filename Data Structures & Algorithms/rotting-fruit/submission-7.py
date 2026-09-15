class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    q.append(((r,c)))
                if grid[r][c]==1:
                    fresh+=1
        directions = [(-1,0), (0, -1), (1, 0), (0,1)]

        while q and fresh>0:
            for i in range(len(q)):
                for d1, d2 in directions:
                    row = q[0][0] + d1
                    col = q[0][1] + d2
                    if 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]==1:
                        q.append((row, col))
                        grid[row][col]=2
                        fresh-=1
                q.popleft()
            time+=1

        return time if fresh == 0 else -1

                

        
                