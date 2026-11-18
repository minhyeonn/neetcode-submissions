class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r, c):
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c]!='O':
                return
            board[r][c]='T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)




        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='O' and (r in [0, len(board)-1] or c in [0,len(board[0])-1]):
                    dfs(r,c)
        


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
                    
