class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def neg(row):
            low, high =0, len(row)
            while(low<high):
                mid = (low+high)//2
                if(row[mid]<0):
                    high = mid
                else:
                    low = mid+1
            return len(row)-low
        
        count = 0
        for row in grid:
            count += neg(row)
        return(count)