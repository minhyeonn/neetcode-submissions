class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))

        dir = [(0,1), (1,0), (0,-1), (-1,0)]

        while q and fresh>0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x,y in dir:
                    row = x+r
                    col = y+c
                    if 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh-=1
            time+=1

        if fresh>0:
            return -1
        else:
            return time
            




