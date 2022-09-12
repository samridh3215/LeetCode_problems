class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        N=len(board)
        for row in range(N):
            for col in range(N):
                if board[row][col]==".":
                    for num in range(1,10):
                        if(self.isValid(num,row,col,board,N)):
                            board[row][col]=str(num)
                            if(self.solveSudoku(board)):
                                return True
                            else:
                                board[row][col]="."
                    return False
        return True
    
    def isValid(self,num,row,col,board,N):
        for i in range(N):
            if str(num) == board[row][i]: return False
            if str(num) == board[i][col]: return False
            if str(num) == board[3*(row//3) +i//3][3*(col//3) +i%3]: return False
        return True