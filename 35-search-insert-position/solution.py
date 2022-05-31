class Solution:
    def searchInsert(self, nums: List[int], key: int) -> int:
        
        i, j = 0, len(nums)-1
        
        while i <= j:
            m = (i + j) // 2
            mid = nums[m]
            if mid > key : j = m - 1
            elif mid < key : i = m + 1
            else : return m
        else:
            return i
