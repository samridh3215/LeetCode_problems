class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        for i in range(1, len(nums)):
            # print(nums[i], type(nums[i]))
            if(nums[i]<nums[i-1]):
                return nums[i]
            if(i==len(nums)-1):
                return nums[0]