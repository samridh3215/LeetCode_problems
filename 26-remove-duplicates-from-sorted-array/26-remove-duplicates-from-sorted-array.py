class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if nums.count(i)>1:
                for j in range(nums.count(i)-1):
                    nums.remove(i)
                    c+=1
        return (len(nums))