class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0,0
        while(r<len(nums)):
            if(nums[l] == nums[r]):
                if(r-l>1):
                    nums.pop(l)
                else:
                    r+=1
            else:
                while(r-l>2):
                    nums.pop(l)
                    l+=1
                l = r
        return len(nums)
            