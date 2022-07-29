class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat[0])
        n = len(mat)
        singlelist = []
        matrix = []
        
        total_elements = m*n
        
        if (r*c!=total_elements):
            return mat
        else:
            for i in mat:
                for j in i:
                    singlelist.append(j)
            for i in range(0, total_elements, c):
                matrix.append(singlelist[i:c+i])
            return matrix
                
            