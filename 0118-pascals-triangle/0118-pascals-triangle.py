class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        base = [[1]]
        if(numRows==1):
            return base
        for i in range(numRows-1):
            row = [1]
            for j in range(i):
                row.append(base[i][j]+base[i][j+1])
            row.append(1)
            base.append(row)
        return base