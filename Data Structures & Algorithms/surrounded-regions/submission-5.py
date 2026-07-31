class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(r, c):
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c]!='O':
                return 
            board[r][c] = "T"

            dfs(r+1,c) 
            dfs(r,c+1) 
            dfs(r-1,c) 
            dfs(r,c-1)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O' and (i==0 or i==len(board)-1) or (j==0 or j==len(board[0])-1):
                    dfs(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                if board[i][j]=='T':
                    board[i][j] = 'O'