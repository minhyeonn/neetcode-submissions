class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:


        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])//2):
                temp = matrix[r][c]
                matrix[r][c] = matrix[r][len(matrix[0]) - c - 1]
                matrix[r][len(matrix[0]) - c - 1] = temp