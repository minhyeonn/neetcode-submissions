class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited_row = collections.defaultdict(set)
        visited_col = collections.defaultdict(set)
        visited_sub_box = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in visited_row[r] or 
                    board[r][c] in visited_col[c] or
                    board[r][c] in visited_sub_box[(r//3,c//3)]):
                    return False
                visited_col[c].add(board[r][c])
                visited_row[r].add(board[r][c])
                visited_sub_box[(r//3,c//3)].add(board[r][c])
                
                
        return True