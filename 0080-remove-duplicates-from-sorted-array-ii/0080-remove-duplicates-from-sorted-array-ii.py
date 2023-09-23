class Solution:
    def removeDuplicates(self, nums) -> int:
        left = 0
        right = 0
        while(right<=len(nums)-1):
            if(nums[left]==nums[right]):
                if(right-left>1):
                    del nums[left]
                else:
                    right+=1
            else:
                left=right
        return len(nums)