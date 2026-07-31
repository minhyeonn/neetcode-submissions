class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i,j, region):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            if board[i][j]=='X':
                return True
            if (i,j) in region:
                return True
            
            region.add((i,j))

            return (dfs(i+1,j,region) and dfs(i,j+1, region)
            and dfs(i-1,j, region) and dfs(i,j-1,region))
                    
            
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    region = set()
                    if dfs(i,j,region):
                        for r, c in region:
                            board[r][c]='X'
