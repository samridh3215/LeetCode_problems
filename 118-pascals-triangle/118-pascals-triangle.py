class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows=[[1]]
        for i in range(1, numRows):
            rows.append([1]*(i+1))
            for c in range(1, i):
                rows[i][c] = rows[i-1][c] + rows[i-1][c-1]
        return rows
