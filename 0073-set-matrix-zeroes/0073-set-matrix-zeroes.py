class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        marked = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    marked.append((i, j))
        for row, col in marked:
            for i in range(n):
                matrix[row][i] = 0
            for i in range(m):
                matrix[i][col] = 0
        
            
