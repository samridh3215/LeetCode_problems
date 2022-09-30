class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i, value in enumerate(nums): 
            findElement = target - nums[i] 
            
            if findElement in record: 
                return [i, record[findElement]] 
            else:
                record[value] = i 